# Generated by Django 4.0.6 on 2023-05-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapApp', '0002_rename_latitude_coralreef_latitudec_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coralreef',
            name='description',
            field=models.CharField(max_length=10000000),
        ),
    ]