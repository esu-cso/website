# Generated by Django 3.2.7 on 2021-10-06 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211006_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
