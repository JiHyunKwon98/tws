# Generated by Django 3.0.3 on 2020-09-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0019_auto_20200904_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='fimage',
            field=models.ImageField(upload_to='Sorlface/%Y', verbose_name='face 이미지'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(upload_to='Sorlphoto/%Y', verbose_name='이미지'),
        ),
    ]
