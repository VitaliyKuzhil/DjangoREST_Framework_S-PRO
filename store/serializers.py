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


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = [
            'id',
            'name',
            'description',
            'rating',
            'owner',
            'status'
        ]
        read_only_fields = ['owner', 'status']
