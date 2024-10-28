# Generated by Django 5.1.1 on 2024-10-28 16:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('url_of_the_news', models.URLField()),
                ('summary', models.TextField(max_length=100)),
                ('image', models.ImageField(blank=True, default='ai_default.jpg', null=True, upload_to='ai_images/')),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
    ]