# Generated by Django 2.1 on 2018-09-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_movieslist_movieimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieslist',
            name='MovieImage',
            field=models.CharField(max_length=800),
        ),
    ]