# Generated by Django 5.0.7 on 2024-09-17 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0004_alter_analysis_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='is_public',
        ),
    ]
