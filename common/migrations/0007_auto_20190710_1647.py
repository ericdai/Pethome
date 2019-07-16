# Generated by Django 2.1.8 on 2019-07-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20190709_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='permission',
            new_name='permissions',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='roles',
        ),
        migrations.AddField(
            model_name='dynamic',
            name='status',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='is_public',
            field=models.BooleanField(default=1),
        ),
    ]
