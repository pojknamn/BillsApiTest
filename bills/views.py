import csv
import io
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import generics, status
from .serializers import BillSerializer


class BillsAPIView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        file = request.FILES['filename'].file
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)

        field_names = ('client_name', 'client_org', 'bill_no',
                       'bill_sum', 'bill_date', 'service')
        errors = []
        for row in reader:
            try:
                if len(row) != len(field_names):
                    raise ValidationError("Некорректное количество полей")
                data = dict(zip(field_names, row))
                serializer = BillSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Exception as e:
                errors.append({'row_wals': {"error": e.args, "row": data}})
        if errors:
            return Response({"Failed": errors}, status=status.HTTP_200_OK)
        return Response({"success": "All data saved"})
