# Generated by Django 4.1.7 on 2023-03-21 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drug', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockRequest',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('request_desc', models.TextField()),
                ('request_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='RequestDrug',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('request_drug_quantity', models.IntegerField()),
                ('request_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.drug')),
            ],
        ),
    ]