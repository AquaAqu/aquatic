# Generated by Django 5.0.2 on 2024-02-10 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishcart', '0002_alter_reg_email_alter_reg_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg',
            old_name='conformpasswords',
            new_name='conformpassword',
        ),
    ]
