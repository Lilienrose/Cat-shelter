# Generated by Django 5.1.6 on 2025-03-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_shelter', '0002_cat_breed_cat_description_cat_deworming_cat_neutered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
