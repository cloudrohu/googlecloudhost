# Generated by Django 4.2.7 on 2023-12-28 10:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_slider_image_id_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='cancellation_and_refund',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='privacy_policy',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='shipping_and_delivery',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='terms_and_conditions',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
