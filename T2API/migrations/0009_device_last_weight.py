# Generated by Django 2.0.2 on 2018-02-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T2API', '0008_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='last_weight',
            field=models.IntegerField(default=-1),
        ),
    ]
