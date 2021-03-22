# Generated by Django 3.0.5 on 2021-03-09 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20210307_1645'),
        ('mainapp', '0020_auto_20210308_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Qauser'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='Users.Qauser'),
        ),
        migrations.AlterField(
            model_name='downvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downvote_user', to='Users.Qauser'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Qauser'),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvote_user', to='Users.Qauser'),
        ),
    ]
