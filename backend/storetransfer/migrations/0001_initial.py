# Generated by Django 4.1.7 on 2023-03-21 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drug', '0001_initial'),
        ('stock', '0001_initial'),
        ('storerequest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTransfer',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('transfer_status', models.BooleanField(default=True)),
                ('transfer_desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocktransfer_stock_from', to='stock.storestock')),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storerequest.stockrequest')),
                ('to_stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocktransfer_stock_to', to='stock.storestock')),
            ],
        ),
        migrations.CreateModel(
            name='TransferDrug',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('transfer_drug_quantity', models.IntegerField()),
                ('transfer_drug_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.drug')),
                ('transfer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storetransfer.stocktransfer')),
            ],
        ),
    ]
