# Generated by Django 4.1.7 on 2023-03-31 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('drug', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('en_name', models.CharField(max_length=25)),
                ('ar_name', models.CharField(max_length=25)),
                ('stock_quantity', models.IntegerField()),
                ('const_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('durg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.drug')),
            ],
        ),
        migrations.CreateModel(
            name='StoreStock',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('store_quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]
