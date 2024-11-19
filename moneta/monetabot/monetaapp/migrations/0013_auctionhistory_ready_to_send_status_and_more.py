# Generated by Django 4.2.16 on 2024-11-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monetaapp', '0012_auctionfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionhistory',
            name='ready_to_send_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='auctionhistory',
            name='received_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='father_name',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='geolocation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_index',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]