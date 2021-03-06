# Generated by Django 3.2.13 on 2022-05-11 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('AccessToken', models.CharField(max_length=10000)),
                ('pageId', models.IntegerField(unique=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Confessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.apps')),
            ],
        ),
        migrations.AddField(
            model_name='apps',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile'),
        ),
    ]
