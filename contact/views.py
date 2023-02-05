from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from contact import serializers
from contact.models import Contact, Numbers


class RegisterContact(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    lookup_field = 'pk'


class RegisterNumber(CreateAPIView):
    queryset = Numbers.objects.all()
    serializer_class = serializers.NumbersPrimarySerializer
    lookup_field = 'pk'


class ContactDetails(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    lookup_field = 'pk'


class ListContacts(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactListSerializer
    lookup_field = 'pk'