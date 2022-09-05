# Generated by Django 4.1.1 on 2022-09-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_date',
            field=models.DateField(verbose_name='Дата платежа'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_no',
            field=models.PositiveIntegerField(verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_sum',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Номер операции'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='client_name',
            field=models.CharField(max_length=50, verbose_name='Имя Клиента'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='client_org',
            field=models.CharField(max_length=150, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='service',
            field=models.CharField(max_length=1000, verbose_name='Наименование услуг'),
        ),
        migrations.AlterUniqueTogether(
            name='bill',
            unique_together={('client_name', 'client_org', 'bill_no')},
        ),
    ]
