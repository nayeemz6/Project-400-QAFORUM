# Generated by Django 3.0.5 on 2021-03-05 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20210220_1248'),
        ('Blog', '0004_auto_20210305_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='overview',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Qauser'),
        ),
    ]
