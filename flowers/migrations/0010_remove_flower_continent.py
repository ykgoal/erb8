# Generated by Django 4.2.17 on 2025-01-12 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0009_flower_continent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flower',
            name='continent',
        ),
    ]