# Generated by Django 5.1.2 on 2025-01-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0016_alter_book_available_copies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
