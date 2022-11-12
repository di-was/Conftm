from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserCreation.as_view(), name='register'),
    path('InOut/<int:type>', Authenticate.as_view(), name='login'),
    path('', Adminpannel.as_view(), name='home'),
    path('confession/<int:pageId>/', Confession.as_view(), name='confession'),
    path('app/creation/', App.as_view()),
    path('confession/view/<int:pageId>/', Viewing.as_view()), # use this to post confession/view/pageid/post/confid/
    path('confession/view/<int:pageId>/deleteAp/', deleteAp),
    path('confession/delete/<int:confessionid>/', deleteConf),
    path('confession/view/<int:pageId>/add/', addconf.as_view()),
    path('<int:pageId>/', addconf.as_view()),
    path('confession/view/<int:pageId>/pso/', Viewing.as_view())
]
