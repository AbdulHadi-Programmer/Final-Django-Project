# Generated by Django 4.1.13 on 2024-10-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
