# Generated by Django 3.1.5 on 2021-10-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
