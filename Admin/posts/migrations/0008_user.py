# Generated by Django 3.2.21 on 2023-09-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]