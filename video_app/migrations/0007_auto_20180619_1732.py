# Generated by Django 2.0.6 on 2018-06-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0006_auto_20180611_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.URLField(),
        ),
    ]
