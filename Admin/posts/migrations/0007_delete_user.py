# Generated by Django 3.2.21 on 2023-09-28 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_liked_post_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
