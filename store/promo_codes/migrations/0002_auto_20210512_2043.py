# Generated by Django 2.2.3 on 2021-05-12 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promo_codes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promocode',
            old_name='disscount',
            new_name='discount',
        ),
    ]
