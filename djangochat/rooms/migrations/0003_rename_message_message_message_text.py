# Generated by Django 4.0.6 on 2024-02-29 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='message_text',
        ),
    ]