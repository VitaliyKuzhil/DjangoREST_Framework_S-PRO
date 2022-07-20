from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from datetime import datetime as date
from .models import Store
from .serializers import CalculatorSerializer, StoreSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


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
        return Response({'Summa': result})


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


class StoreApiView(APIView):

    def get(self, request, format=None):
        """
        Return a list of all stores.
        """
        stores = Store.objects.filter(owner__isnull=True)
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


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class UserStoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        get_store = self.get_object()
        if get_store.status == "deactivated":
            get_store.status = "active"
            get_store.save()
        serializer = self.get_serializer(get_store)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_deactivated(self, request, pk=None):
        get_store = self.get_object()
        if get_store.status == "active":
            get_store.status = "deactivated"
            get_store.save()
        serializer = self.get_serializer(get_store)
        return Response(serializer.data)


class AdminStoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['name', 'owner__id']
    ordering_fields = ['rating']

    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        get_store = self.get_object()
        if get_store.status == "in_review":
            get_store.status = "active"
            get_store.save()
        serializer = self.get_serializer(get_store)
        return Response(serializer.data)
