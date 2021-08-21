# Generated by Django 3.2.5 on 2021-07-27 08:29

import BackPyTeam.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPyTeam', '0004_alter_teammembers_personal_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='photo',
            field=models.ImageField(blank=True, help_text='Image size: 245 × 247', null=True, upload_to=BackPyTeam.models.upload_image_path),
        ),
    ]
