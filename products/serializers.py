from rest_framework.serializers import ModelSerializer
from .models import *

class prodsales_serializer(ModelSerializer):
    class Meta():
        model=prodsales
        fields='__all__'

class cart_serializer(ModelSerializer):
    class Meta():
        model=cart
        fields='__all__'


