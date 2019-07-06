from rest_framework import serializers
from testapp.models import Hyderabad

class HyderabadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hyderabad
        fields='__all__'