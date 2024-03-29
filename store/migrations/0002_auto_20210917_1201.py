# Generated by Django 3.2.7 on 2021-09-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priceplandetail',
            name='paymenttype',
        ),
        migrations.RemoveField(
            model_name='priceplandetail',
            name='priceplan',
        ),
        migrations.AddField(
            model_name='priceplan',
            name='annual_instalment_amount',
            field=models.FloatField(default=1000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='annual_instalments',
            field=models.IntegerField(default=1000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='downpayment',
            field=models.FloatField(default=1000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='final_payment_amount',
            field=models.FloatField(default=1000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='halfyearly_instalment_amount',
            field=models.FloatField(default=500000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='halfyearly_instalments',
            field=models.IntegerField(default=500000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='monthly_instalment_amount',
            field=models.FloatField(default=250000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='monthly_instalments',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='quarterly_instalment_amount',
            field=models.FloatField(default=500000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priceplan',
            name='quarterly_instalments',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Paymenttype',
        ),
        migrations.DeleteModel(
            name='Priceplandetail',
        ),
    ]
