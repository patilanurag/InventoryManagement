# Generated by Django 3.1.2 on 2020-11-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorrecord',
            name='recieving_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
