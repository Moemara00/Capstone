# Generated by Django 5.1.2 on 2025-01-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0012_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.IntegerField( unique=True,default=0),
        ),
    ]
