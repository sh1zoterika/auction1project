# Generated by Django 4.2.16 on 2024-11-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monetaapp', '0006_alter_auction_seller_alter_auctionhistory_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10),
        ),
    ]