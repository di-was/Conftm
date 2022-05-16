# Generated by Django 3.2.13 on 2022-05-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_apps_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confessed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AlterModelOptions(
            name='confessions',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='apps',
            name='url',
            field=models.URLField(default='https://127.0.0.1:8000/'),
        ),
    ]
