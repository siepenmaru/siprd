# Generated by Django 3.2.7 on 2021-09-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210922_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nip',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
