# Generated by Django 2.0.2 on 2018-02-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T2API', '0013_auto_20180217_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceoffer',
            name='image_url',
            field=models.TextField(default=None, null=True),
        ),
    ]
