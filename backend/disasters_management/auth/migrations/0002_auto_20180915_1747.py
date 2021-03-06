# Generated by Django 2.1.1 on 2018-09-15 17:47

import auth.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('my.auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='center_point',
            field=djongo.models.fields.EmbeddedModelField(model_container=auth.models.GeoJSON, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='lang',
            field=models.FloatField(default=5.25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='lat',
            field=models.FloatField(default=2.65),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.IntegerField(choices=[('o', 'organizaation'), ('h', 'human')], null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
    ]
