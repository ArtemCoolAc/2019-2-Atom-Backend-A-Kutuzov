# Generated by Django 2.2.5 on 2019-11-06 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20191028_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'chat', 'verbose_name_plural': 'chats'},
        ),
    ]
