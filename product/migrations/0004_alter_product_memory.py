# Generated by Django 4.2.7 on 2023-12-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_discount_alter_product_m_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='memory',
            field=models.CharField(choices=[('Micro Business Plan', 'Micro Business Plan'), ('Small Business Plan', 'Small Business Plan'), ('Medium Business Plan', 'Medium Business Plan')], default='None', max_length=25),
        ),
    ]
