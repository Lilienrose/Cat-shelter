# Generated by Django 5.1.6 on 2025-03-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_shelter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='breed',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cat',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='deworming',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=5),
        ),
        migrations.AddField(
            model_name='cat',
            name='neutered',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=5),
        ),
        migrations.AddField(
            model_name='cat',
            name='sex',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male')], default='y', max_length=5),
        ),
        migrations.AddField(
            model_name='cat',
            name='vaccination',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=5),
        ),
    ]
