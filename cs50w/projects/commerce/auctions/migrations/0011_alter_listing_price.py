# Generated by Django 4.1.3 on 2022-12-06 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_bid_bid_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_offer', to='auctions.bid'),
        ),
    ]
