# Generated by Django 2.0.2 on 2018-02-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T2API', '0005_auto_20180217_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='polling_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='secret_key',
            field=models.TextField(default=None, null=True),
        ),
    ]
