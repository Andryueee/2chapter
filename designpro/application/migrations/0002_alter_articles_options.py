# Generated by Django 4.2.7 on 2023-11-10 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]