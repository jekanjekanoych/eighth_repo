# Generated by Django 4.2.1 on 2023-05-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=200),
        ),
    ]
