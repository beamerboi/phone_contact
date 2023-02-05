from rest_framework import serializers
from .models import Contact, Numbers


class NumbersPrimarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ('phone_number',)

    def validate(self, data):
        print(data)
        return data


class ContactSerializer(serializers.ModelSerializer):
    numbers = NumbersPrimarySerializer(many=True)

    class Meta:
        model = Contact
        fields = ('contact_name', 'numbers')

    def create(self, validated_data):
        print(validated_data)
        numbers_data = validated_data.pop('numbers')
        contact = Contact.objects.create(**validated_data)
        for number_data in numbers_data:
            Numbers.objects.create(contact=contact, **number_data)
        return contact


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact_name',)
