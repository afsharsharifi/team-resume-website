# Generated by Django 3.2.2 on 2021-07-22 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPySlider', '0002_slider_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='UnderText',
            field=models.CharField(default='welcome', max_length=20),
        ),
    ]
