# Generated by Django 3.1.4 on 2022-04-19 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0007_auto_20220419_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replie',
            name='image',
        ),
    ]