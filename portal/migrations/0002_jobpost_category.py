# Generated by Django 3.2.14 on 2022-11-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]