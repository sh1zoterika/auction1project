# Generated by Django 4.2.16 on 2024-11-12 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monetaapp', '0002_rename_product_name_auctionlot_lot_auction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionhistory',
            name='lots',
        ),
    ]