# Generated by Django 2.0.2 on 2018-02-17 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('T2API', '0004_auto_20180217_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='T2API.Product'),
        ),
    ]
