# Generated by Django 2.1.8 on 2019-07-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20190710_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=1),
        ),
    ]
