# Generated by Django 3.2.7 on 2021-09-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210917_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceplan',
            name='price',
            field=models.IntegerField(default=2000000),
            preserve_default=False,
        ),
    ]
