# Generated by Django 4.1.1 on 2022-10-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_associate_associates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
