# Generated by Django 3.2.2 on 2021-07-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPyService', '0003_alter_designs_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designs',
            name='title',
            field=models.CharField(choices=[('UI', 'PORN'), ('UX', 'UX')], max_length=50),
        ),
    ]
