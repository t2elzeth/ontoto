# Generated by Django 3.1.3 on 2020-11-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0002_auto_20201114_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]
