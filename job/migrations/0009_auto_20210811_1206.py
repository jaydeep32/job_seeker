# Generated by Django 3.2.4 on 2021-08-11 12:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20210811_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 11, 12, 6, 33, 324986, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='job',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
