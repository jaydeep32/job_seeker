# Generated by Django 3.2.4 on 2021-08-12 04:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210812_0421'),
        ('job', '0021_alter_job_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.profile'),
        ),
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 12, 4, 21, 10, 691224, tzinfo=utc)),
        ),
    ]