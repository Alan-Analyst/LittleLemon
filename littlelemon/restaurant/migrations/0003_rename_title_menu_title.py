# Generated by Django 5.0.3 on 2024-03-20 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Title',
            new_name='title',
        ),
    ]
