# Generated by Django 4.2.2 on 2023-07-11 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("comments", "0001_initial"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts_comment",
                to="posts.post",
            ),
        ),
    ]
