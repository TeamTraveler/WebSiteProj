# Generated by Django 4.1.1 on 2022-11-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0009_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name_plural": "Categories1",
                "db_table": "category",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Category2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name_plural": "Categories2",
                "db_table": "category",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
