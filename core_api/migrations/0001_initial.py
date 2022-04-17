# Generated by Django 4.0.4 on 2022-04-15 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField()),
                ('entry_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Exit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exit_date', models.DateField()),
                ('exit_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_code', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=2)),
                ('capacity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HKUMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hku_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('entered_venue', models.ManyToManyField(related_name='entered_venue', through='core_api.Entry', to='core_api.venue')),
                ('exited_venue', models.ManyToManyField(related_name='exited_venue', through='core_api.Exit', to='core_api.venue')),
            ],
        ),
        migrations.AddField(
            model_name='exit',
            name='exit_hku_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_api.hkumember'),
        ),
        migrations.AddField(
            model_name='exit',
            name='exit_venue_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_api.venue'),
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_hku_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_api.hkumember'),
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_venue_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_api.venue'),
        ),
    ]