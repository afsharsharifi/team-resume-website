# Generated by Django 3.2.5 on 2021-07-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPyBlog', '0002_blog_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
