# Generated by Django 3.0 on 2020-02-06 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200206_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=1, max_length=20),
        ),
    ]