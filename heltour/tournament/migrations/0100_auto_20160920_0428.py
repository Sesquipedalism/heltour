# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 04:28


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0099_alternate_priority_date_override'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('time', models.DateTimeField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.League')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='privateurlauth',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
