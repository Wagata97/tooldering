# Generated by Django 4.1.1 on 2022-10-11 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_associates_associate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Associate',
            new_name='Associates',
        ),
    ]
