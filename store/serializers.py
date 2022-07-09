from rest_framework import serializers
from store.models import Store


class CalculatorSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    operation = serializers.ChoiceField(choices=['plus', 'minus', 'multi', 'division'])
    number2 = serializers.IntegerField()

    def validate(self, validated_data):

        if validated_data['operation'] == 'division' and validated_data['number2'] == 0:
            raise serializers.ValidationError('Ви не можете поділити на 0')

        return validated_data


class StoreSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    rating = serializers.IntegerField()

    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        return store
