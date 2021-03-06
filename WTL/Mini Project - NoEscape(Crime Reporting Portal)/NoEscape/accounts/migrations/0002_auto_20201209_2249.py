# Generated by Django 3.1.3 on 2020-12-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='address',
            field=models.CharField(default='add address', max_length=200),
        ),
        migrations.AddField(
            model_name='applicant',
            name='video',
            field=models.URLField(default='https://avcd/ssaa'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(default='abc@edf.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='name',
            field=models.CharField(default='add name', max_length=100),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.IntegerField(default='211313131'),
        ),
    ]
