# Generated by Django 4.0.2 on 2022-02-22 22:55

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('attributes', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=255)),
                ('product_dir', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=120)),
                ('main_file', models.FileField(upload_to=core.models.upload_file_products)),
                ('file_size', models.IntegerField()),
                ('file_extension', models.CharField(max_length=10)),
                ('official_product', models.BooleanField(default=False)),
                ('survey', models.CharField(max_length=255)),
                ('pz_code', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='core.producttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
