# Generated by Django 3.1.2 on 2020-11-02 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='')),
                ('size', models.PositiveIntegerField(verbose_name='Размер')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
