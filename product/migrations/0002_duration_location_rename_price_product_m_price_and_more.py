# Generated by Django 4.2.7 on 2023-12-23 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='m_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='minamount',
        ),
        migrations.RemoveField(
            model_name='variants',
            name='color',
        ),
        migrations.RemoveField(
            model_name='variants',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='memory',
            field=models.CharField(choices=[('1GB MEMORY', '1GB MEMORY'), ('2GB MEMORY', '2GB MEMORY'), ('3GB MEMORY', '3GB MEMORY'), ('4GB MEMORY', '4GB MEMORY'), ('6GB MEMORY', '6GB MEMORY'), ('8GB MEMORY', '8GB MEMORY'), ('12GB MEMORY', '12GB MEMORY'), ('16GB MEMORY', '16GB MEMORY')], default='None', max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Duration', 'Duration'), ('Location', 'Location'), ('Duration-Location', 'Duration-Location')], default='None', max_length=25),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AddField(
            model_name='product',
            name='duration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.duration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variants',
            name='duration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.duration'),
        ),
        migrations.AddField(
            model_name='variants',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.location'),
        ),
    ]
