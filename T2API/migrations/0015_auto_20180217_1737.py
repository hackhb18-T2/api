# Generated by Django 2.0.2 on 2018-02-17 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('T2API', '0014_auto_20180217_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prices',
        ),
        migrations.AddField(
            model_name='priceoffer',
            name='prices',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='T2API.Product'),
        ),
    ]
