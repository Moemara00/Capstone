# Generated by Django 5.1.2 on 2025-01-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_alter_book_available_copies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='check_out_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
