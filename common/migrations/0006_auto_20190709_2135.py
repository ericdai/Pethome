# Generated by Django 2.1.8 on 2019-07-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20190709_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catvari',
            old_name='vari_name',
            new_name='cat_vari_name',
        ),
        migrations.AlterField(
            model_name='catvari',
            name='price',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='catvari',
            name='weight',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='dogvari',
            name='price',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='dogvari',
            name='weight',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
