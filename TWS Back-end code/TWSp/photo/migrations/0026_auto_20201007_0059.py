# Generated by Django 3.0.3 on 2020-10-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0025_auto_20201006_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='no',
            field=models.IntegerField(blank=True, null=True, verbose_name='출고번호'),
        ),
    ]
