# Generated by Django 3.2.16 on 2024-02-21 06:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0005_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.branch')),
            ],
        ),
    ]
