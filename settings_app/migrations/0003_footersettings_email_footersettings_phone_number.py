# Generated by Django 5.0 on 2023-12-26 17:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0002_footerlinks_footersettings_socialsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='footersettings',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footersettings',
            name='phone_number',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]