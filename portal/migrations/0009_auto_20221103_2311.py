# Generated by Django 3.2.14 on 2022-11-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20221102_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='expiry_date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='posted_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='posted_on',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
