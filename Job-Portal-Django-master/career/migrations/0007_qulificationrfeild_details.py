# Generated by Django 3.2.16 on 2024-02-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0006_coursedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='qulificationrfeild',
            name='details',
            field=models.CharField(default='', max_length=500),
        ),
    ]