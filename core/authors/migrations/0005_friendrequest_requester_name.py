# Generated by Django 2.1.5 on 2019-02-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20190216_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='requester_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
