# Generated by Django 3.1.3 on 2020-12-11 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201211_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={},
        ),
        migrations.RemoveField(
            model_name='video',
            name='date_created',
        ),
    ]
