# Generated by Django 4.0.1 on 2022-01-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.TextField(blank=True, null=True, verbose_name='태그'),
        ),
    ]
