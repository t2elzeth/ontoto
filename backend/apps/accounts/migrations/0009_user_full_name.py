# Generated by Django 3.1.3 on 2020-11-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201118_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]