# Generated by Django 3.2.17 on 2023-03-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
