# Generated by Django 3.2.2 on 2021-07-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPySlider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default='slider', max_length=100),
        ),
    ]
