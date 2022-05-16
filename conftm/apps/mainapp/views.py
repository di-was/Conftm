from django.http import HttpResponseNotFound, HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from conftm.apps.mainapp.models import *
from django.http import JsonResponse
import json
from conftm.apps.mainapp.forms import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import ast
from django.contrib.auth.decorators import login_required
from django.contrib.auth import load_backend
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import facebook
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class Authenticate(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, "login.html", {'form': form})

    def post(self, request, *args, **kwargs):
        data = ast.literal_eval(request.body.decode())
        username, password = data['username'], data['password']

        if int(self.kwargs['type']) == 0:
            try:
                user = User.objects.get(username=username, password=password)
            except:
                return HttpResponse("Either username or password is incorrect", status=400)
        else:
            user = True
        if user != None:
            if int(self.kwargs['type']) == 0:
                login(request, user)
                return HttpResponse("https://conftm.herokuapp.com/", status=200)
            else:
                logout(request)
                return HttpResponse(status=200)


class UserCreation(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, "register.html", {"form": form})

    def post(self, request, *args, **kwargs):

        userform = UserForm(ast.literal_eval(request.body.decode()))
        if userform.is_valid():
            print("TRue")
            userform.save()
            instance = UserProfile(user=User.objects.get(username=userform.cleaned_data['username'], password=userform.cleaned_data['password']))
            instance.save()
            return HttpResponse(f"{instance.user.username} created and logged in", status=200)
        else:
            return HttpResponseServerError()


class Confession(View):

    def get(self, request, *args, **kwargs):
        form = ConfessionsForm()
        return render(request, "confession.html", {"form": form})

    def post(self, request, *args, **kwargs):
       data = ast.literal_eval(request.body.decode())
       parent = Apps.objects.get(pageId=int(self.kwargs['pageId']))
       data['parent'] = parent
       confessionform = ConfessionsForm(data)
       if confessionform.is_valid():
           confessionform.save()
           return HttpResponse(status=200)
       else:
            return HttpResponse(status=400)

class App(View):
    def get(self, request, *args, **kwargs):
        form = Appform()
        return render(request, 'Appcreation.html', {'form': form})

    def post(self, request, *args, **kwargs):
        data = ast.literal_eval((request.body.decode()))
        def get_user(request):
            if not hasattr(request, '_cached_user'):
                request._cached_user = auth.get_user(request)
            return request._cached_user
        data['parent'] = get_user(request).userprofile
        appfprm = Appform(data)
        if appfprm.is_valid():
            appfprm.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@method_decorator(login_required(login_url="https://conftm.herokuapp.com/InOut/0"), name="dispatch")
class Adminpannel(View):
    def get(self, request, *args, **kwargs):
        app = {}
        set = request.user.userprofile.apps_set.all()
        for x in range(0, len(set)):
            app[str(x)] = set[x].info()
        data = {'user': request.user.username, 'app': app}
        return render(request, "home.html", data)

class Viewing(View):
    def get(self, request, *args, **kwargs):
        apppageId = self.kwargs['pageId']
        if request.user == Apps.objects.get(pageId=apppageId).parent.user:
            confessionslist = Confessions.objects.all().filter(parent=Apps.objects.get(pageId=apppageId))
            data = {}
            for x in confessionslist:
                data[x.id] = {'content' : x.content, 'id': x.id}
            return render(request, 'confessionview.html', {'data' : data})
        else:
            return HttpResponse(status=403)

    def post(self, request, *args, **kwargs):
        pageId = self.kwargs['pageId']
        app = Apps.objects.get(pageId=pageId)
        access_token = app.AccessToken
        Idapp = app.pageId
        confessionid = Confessions.objects.get(id=ast.literal_eval(request.body.decode())['id'])
        graph = facebook.GraphAPI(access_token=access_token)
        graph.put_object(parent_object=Idapp, connection_name="feed", message= f"Confession #{ast.literal_eval(request.body.decode())['id']}  : " + confessionid.content)
        print(ast.literal_eval(request.body.decode()))
        confessedObject = Confessed(content=confessionid.content)
        confessionid.delete()
        confessedObject.save()
        return HttpResponse(status=200)


def deleteConf(request, confessionid):
    if request.method == 'POST':
        target = Confessions.objects.get(id=int(confessionid))
        if target.parent.parent.user == request.user:
            target.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponseServerError()
    else:
        return HttpResponseNotFound()


def deleteAp(request, pageId):
    if request.method == 'POST':
        target = Apps.objects.get(pageId=int(pageId))
        if request.user.userprofile == target.parent:
            target.delete()
            return HttpResponse("ok", status=200)
        else:
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=403)

@method_decorator(csrf_exempt, name='dispatch')
class addconf(View):

    def get(self, request, *args, **kwargs ):
        pageId = self.kwargs['pageId']
        app = Apps.objects.get(pageId=int(pageId))
        form = ConfessionsForm()
        return render(request, 'confession.html', {'form': form, 'name': app.name})

    def post(self, request, *args, **kwargs):
        app = Apps.objects.get(pageId=int(self.kwargs['pageId']))
        data = ast.literal_eval(request.body.decode())
        data['parent'] = app
        form = ConfessionsForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)

