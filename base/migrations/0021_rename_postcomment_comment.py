# Generated by Django 4.2.13 on 2024-06-24 13:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0020_postcomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostComment',
            new_name='Comment',
        ),
    ]
