# Generated by Django 3.0.5 on 2021-03-05 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20210220_1248'),
        ('mainapp', '0005_auto_20210305_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_name',
            field=models.CharField(default='nayeem', max_length=12),
            preserve_default=False,
        ),
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