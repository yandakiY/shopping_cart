# Generated by Django 4.2.3 on 2023-08-30 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart_app', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
