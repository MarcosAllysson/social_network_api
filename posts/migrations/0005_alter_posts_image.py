# Generated by Django 3.2.8 on 2021-10-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_posts_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='posts', verbose_name='image'),
        ),
    ]
