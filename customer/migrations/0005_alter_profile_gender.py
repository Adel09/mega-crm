# Generated by Django 3.2.5 on 2022-05-31 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
    ]
