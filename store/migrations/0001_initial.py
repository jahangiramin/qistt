# Generated by Django 3.2.7 on 2021-09-16 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paymenttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Priceplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sku', models.CharField(max_length=255)),
                ('ispublic', models.BooleanField()),
                ('category', models.ManyToManyField(to='store.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Priceplandetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('paymenttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.paymenttype')),
                ('priceplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.priceplan')),
            ],
        ),
        migrations.AddField(
            model_name='priceplan',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AddField(
            model_name='priceplan',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.term'),
        ),
    ]
