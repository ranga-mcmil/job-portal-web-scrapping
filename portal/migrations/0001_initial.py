# Generated by Django 3.2.14 on 2022-11-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posted_by', models.CharField(max_length=100)),
                ('link_to_job', models.URLField()),
                ('expiry_date', models.CharField(max_length=30)),
                ('posted_on', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]
