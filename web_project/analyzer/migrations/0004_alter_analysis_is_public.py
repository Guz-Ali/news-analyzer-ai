# Generated by Django 5.0.7 on 2024-09-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0003_analysis_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='is_public',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
