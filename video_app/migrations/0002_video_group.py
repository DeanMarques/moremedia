# Generated by Django 2.0.4 on 2018-05-03 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='video_app.Group'),
            preserve_default=False,
        ),
    ]
