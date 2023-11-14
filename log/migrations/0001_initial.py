# Generated by Django 5.0b1 on 2023-11-09 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(max_length=20)),
                ('objeto_afetado', models.CharField(blank=True, max_length=255, null=True)),
                ('mensagem', models.CharField(blank=True, max_length=255, null=True)),
                ('dados_antes', models.JSONField(blank=True, null=True)),
                ('dados_depois', models.JSONField(blank=True, null=True)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
