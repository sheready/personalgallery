# Generated by Django 2.2.6 on 2020-08-03 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='posts.Location'),
        ),
    ]
