# Generated by Django 3.2.8 on 2021-10-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211021_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='publications', verbose_name='image'),
        ),
    ]