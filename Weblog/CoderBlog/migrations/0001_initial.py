# Generated by Django 2.2 on 2022-06-21 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=400)),
                ('author', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='userText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=400)),
                ('author', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
