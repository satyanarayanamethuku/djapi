from testapp.api.serializers import HyderabadSerializer
from testapp.models import Hyderabad
from rest_framework import viewsets



class HydJobsCRUD(viewsets.ModelViewSet):
    queryset=Hyderabad.objects.all()
    serializer_class=HyderabadSerializer
