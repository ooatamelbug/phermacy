# Generated by Django 4.1.7 on 2023-03-21 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('en_brand_name', models.CharField(max_length=25)),
                ('ar_brand_name', models.CharField(max_length=25)),
                ('chemical_name', models.CharField(max_length=25)),
                ('national_code', models.CharField(max_length=25)),
                ('manufacture', models.CharField(max_length=25)),
                ('drug_dose', models.CharField(max_length=25)),
                ('drug_usage', models.CharField(max_length=25)),
                ('main_uom', models.CharField(max_length=25)),
                ('small_uom', models.CharField(max_length=25)),
                ('drug_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.classes')),
            ],
        ),
    ]
