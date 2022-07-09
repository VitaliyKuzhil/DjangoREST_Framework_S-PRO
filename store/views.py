from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from datetime import datetime as date
from .serializers import CalculatorSerializer, StoreSerializer

from rest_framework.views import APIView
from .models import Store
from rest_framework.status import HTTP_201_CREATED


@api_view(http_method_names=['GET'])
def today(request):
    date_today = {
        'date': date.today().date(),
        'year': date.today().year,
        'month': date.today().month,
        'day': date.today().day,
    }
    return Response(date_today)


# today/


@api_view(http_method_names=['GET'])
def hello(request):
    hello_msg = {'message': 'Hello World'}
    return Response(hello_msg)


# hello_world/


@api_view(http_method_names=['GET'])
def name(request, name_of_hacker):
    return_name = {"name": name_of_hacker.title()}
    return Response(return_name)


# my_name/vitaliy kuzhil


@api_view(http_method_names=['GET', 'POST'])
def calculator(request):
    if request.method == 'GET':
        params = {'number1': 5, 'operation': "multi", 'number2': 3}
        return Response(params)
    # calculator/

    if request.method == 'POST':
        serializer = CalculatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        calc_valid = serializer.validated_data

        result = 0
        if calc_valid['operation'] == 'plus':
            result = calc_valid['number1'] + calc_valid['number2']
        elif calc_valid['operation'] == 'minus':
            result = calc_valid['number1'] - calc_valid['number2']
        elif calc_valid['operation'] == 'multi':
            result = calc_valid['number1'] * calc_valid['number2']
        elif calc_valid['operation'] == 'div':
            result = calc_valid['number1'] / calc_valid['number2']
        """
        {
        "number1": 10,
        "operation": "division",
        "number2": 0
        }

        {
        "number1": 5,
        "operation": "multi",
        "number2": 3
        }
        """
        return Response({'Summa': result})


class StoreApiView(APIView):

    def get(self, request, format=None):
        """
        Return a list of all stores.
        """
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    # store /

    def post(self, request, format=None):
        """
        Create store in stores.
        """
        serializers = StoreSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(status=HTTP_201_CREATED, data=serializers.data)

    """
    {
    "name": "Store1",
    "description": "Store1_description",
    "rating": 95
    }
    """

