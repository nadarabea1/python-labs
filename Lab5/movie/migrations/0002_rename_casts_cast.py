# Generated by Django 4.2.1 on 2023-06-01 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Casts',
            new_name='Cast',
        ),
    ]