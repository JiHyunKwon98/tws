# Generated by Django 3.0.3 on 2020-10-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0022_auto_20201005_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='no',
            field=models.CharField(max_length=16, null=True, verbose_name='출고번호'),
        ),
    ]
