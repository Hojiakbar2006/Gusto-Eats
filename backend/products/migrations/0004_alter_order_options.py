# Generated by Django 5.0.1 on 2024-01-26 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_feedback_alter_order_totalprice_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-createdAt']},
        ),
    ]