# Generated by Django 3.0.4 on 2020-03-10 17:18

from django.db import migrations
from django.conf import settings


def create_data(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User(pk=1, username="auth0user", is_active=True , email="sensor14@list.ru")
    user.save()


class Migration(migrations.Migration):
    dependencies = [
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
