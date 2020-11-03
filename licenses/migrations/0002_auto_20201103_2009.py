# Generated by Django 3.1.3 on 2020-11-03 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='license_assigned_to',
            field=models.CharField(blank=True, default='License is free', max_length=50),
        ),
        migrations.AlterField(
            model_name='license',
            name='purchase_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='license',
            name='renewal_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]