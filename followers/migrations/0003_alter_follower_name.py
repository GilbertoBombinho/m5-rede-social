# Generated by Django 4.2.2 on 2023-07-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("followers", "0002_alter_follower_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follower",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
