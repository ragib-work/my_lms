# Generated by Django 5.1.4 on 2025-01-07 11:04

import apps.courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.courses.models.handle_upload)),
                ('access', models.CharField(choices=[('any', 'Anyone'), ('email_required', 'Email required'), ('purchase_required', 'Purchase required'), ('user_required', 'User required')], default='any', max_length=20)),
                ('status', models.CharField(choices=[('pub', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='draft', max_length=10)),
            ],
        ),
    ]
