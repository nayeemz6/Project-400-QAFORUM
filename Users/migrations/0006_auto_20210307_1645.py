# Generated by Django 3.0.5 on 2021-03-07 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20210220_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qauser',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='qauser',
            name='links',
        ),
    ]
