# Generated by Django 5.0.7 on 2024-09-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_alter_analysis_findings'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
