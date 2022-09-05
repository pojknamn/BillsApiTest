# Generated by Django 4.1.1 on 2022-09-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, verbose_name='client')),
                ('client_org', models.CharField(max_length=150, verbose_name='org')),
                ('bill_no', models.PositiveIntegerField(verbose_name='sum')),
                ('bill_sum', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bill_date', models.DateTimeField()),
                ('service', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
