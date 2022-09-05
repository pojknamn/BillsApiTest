from django.db import models

class Bill(models.Model):
    client_name = models.CharField(verbose_name='Имя Клиента', max_length=50)
    client_org = models.CharField(verbose_name='Организация', max_length=150)
    bill_no = models.PositiveIntegerField(verbose_name='Номер операции')
    bill_sum = models.DecimalField(verbose_name='Сумма', decimal_places=2, max_digits=12)
    bill_date = models.DateField(verbose_name='Дата платежа')
    service = models.CharField(verbose_name='Наименование услуг', max_length=1000, blank=False,
                               null=False)

    class Meta:
        unique_together = ('client_name', 'client_org', "bill_no")
