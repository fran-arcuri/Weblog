# Generated by Django 2.2 on 2022-07-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoderBlog', '0010_remove_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
