# Generated by Django 4.2.7 on 2023-12-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='image_id',
        ),
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
