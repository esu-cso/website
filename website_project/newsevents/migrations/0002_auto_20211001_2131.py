# Generated by Django 3.1.5 on 2021-10-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsevents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
