import datetime

from rest_framework import serializers
from .models import Bill


def name_validator(name):
    if name.strip():
        return name
    raise serializers.ValidationError('there is empty name')


def service_validator(service):
    if service.replace('-', '').strip():
        return service
    raise serializers.ValidationError('there is empty service')


def number_validator(num):
    try:
        num = float(num)
    except ValueError:
        raise serializers.ValidationError('Не валидные данные')
    return num


def int_validator(num):
    try:
        num = int(num)
    except ValueError:
        raise serializers.ValidationError('Не валидные данные')
    return num


def date_validate(date):
    try:
        date = datetime.datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        raise serializers.ValidationError('Некорректная дата')
    return date


class BillSerializer(serializers.Serializer):
    client_name = serializers.CharField(validators=[name_validator])
    client_org = serializers.CharField(validators=[name_validator])
    service = serializers.CharField(validators=[service_validator])
    bill_no = serializers.IntegerField(validators=[int_validator])
    bill_sum = serializers.DecimalField(validators=[number_validator], max_digits=12,
                                        decimal_places=2)
    bill_date = serializers.DateField(input_formats=['%d.%m.%Y'])

    def create(self, validated_data):
        bill = Bill.objects.create(**validated_data)
        return bill

    class Meta:
        model = Bill
        fields = '__all__'
