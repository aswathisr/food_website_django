# Generated by Django 3.2.4 on 2021-06-14 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0009_alter_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
