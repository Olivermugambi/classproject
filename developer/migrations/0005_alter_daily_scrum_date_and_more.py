# Generated by Django 4.1.3 on 2022-12-16 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0004_alter_daily_scrum_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_scrum',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 878520), verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 869518), verbose_name='registration date'),
        ),
        migrations.AlterField(
            model_name='developer_status',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 867520), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 871520), verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 871520), verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='sprint_backlog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 873519), verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='sprint_backlog_allocations',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 876521), verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='sprint_retrospective',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 883520), verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='sprint_review',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 18, 18, 12, 881521), verbose_name='creation date'),
        ),
    ]
