# Generated by Django 4.1.3 on 2022-12-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libros", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="libro",
            name="descripcion",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
