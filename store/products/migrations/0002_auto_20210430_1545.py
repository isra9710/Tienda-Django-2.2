# Generated by Django 2.2.3 on 2021-04-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tittle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='slag',
            field=models.SlugField(default='Hola', unique=True),
            preserve_default=False,
        ),
    ]