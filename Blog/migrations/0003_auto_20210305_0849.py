# Generated by Django 3.0.5 on 2021-03-05 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20210220_1248'),
        ('Blog', '0002_auto_20210305_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Qauser'),
        ),
    ]
