# Generated by Django 3.2.8 on 2021-10-22 18:32

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to=posts.models.get_file_path, verbose_name='image'),
        ),
    ]
