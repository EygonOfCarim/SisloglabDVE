# Generated by Django 5.0b1 on 2023-11-14 15:28

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_userprofile_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_by',
            field=models.ForeignKey(default=datetime.datetime(2023, 11, 14, 12, 28, 55, 150734), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_by',
            field=models.ForeignKey(default=datetime.datetime(2023, 11, 14, 12, 28, 55, 150734), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
