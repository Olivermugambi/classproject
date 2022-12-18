# Generated by Django 4.1.3 on 2022-12-17 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customermanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_profile',
            old_name='url',
            new_name='customer_url',
        ),
        migrations.AlterField(
            model_name='contact_person',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 741848), verbose_name='registration date'),
        ),
        migrations.AlterField(
            model_name='contact_person_status',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 740849), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='customer_message',
            name='date_sent',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 746848), verbose_name='date sent'),
        ),
        migrations.AlterField(
            model_name='customer_product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 750848), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='customer_profile',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 738848), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='customer_status',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 736848), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='customer_type',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 734849), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='message_status',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 745850), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='message_type',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 743848), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='product_requirements',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 752850), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 15, 5, 55, 748847), verbose_name='date created'),
        ),
    ]