# Generated by Django 2.0.2 on 2018-02-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T2API', '0003_auto_20180217_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='battery_status',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='resolution',
            field=models.CharField(default=None, max_length=15, null=True),
        ),
    ]
