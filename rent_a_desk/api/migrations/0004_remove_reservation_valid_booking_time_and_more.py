# Generated by Django 4.0 on 2021-12-26 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_reservation_valid_booking_time'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='reservation',
            name='valid_booking_time',
        ),
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.CheckConstraint(check=models.Q(('booked_from__gte', datetime.datetime(2021, 12, 26, 12, 29, 8, 359699))), name='valid_booking_time'),
        ),
    ]
