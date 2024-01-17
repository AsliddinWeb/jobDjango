# Generated by Django 5.0 on 2023-12-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='files',
        ),
        migrations.AddField(
            model_name='job',
            name='file',
            field=models.FileField(default=2, upload_to='files'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='JobFile',
        ),
    ]
