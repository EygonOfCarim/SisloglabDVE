# Generated by Django 4.2.6 on 2023-10-31 14:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_alter_userprofile_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_by',
            field=models.ForeignKey(default=datetime.datetime(2023, 10, 31, 11, 48, 10, 573789), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_by',
            field=models.ForeignKey(default=datetime.datetime(2023, 10, 31, 11, 48, 10, 573789), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
