# Generated by Django 4.1.7 on 2023-03-21 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shelf', '0001_initial'),
        ('stock', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelfdrug',
            name='store_stock_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.storestock'),
        ),
        migrations.AddField(
            model_name='shelf',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]