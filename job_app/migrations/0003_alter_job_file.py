# Generated by Django 5.0 on 2023-12-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0002_remove_job_files_job_file_delete_jobfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
