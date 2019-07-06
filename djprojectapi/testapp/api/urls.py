from testapp.api.views import HydJobsCRUD
from django.conf.urls import url,include
from rest_framework import routers
router=routers.DefaultRouter()
router.register('hydjobsinfo',HydJobsCRUD)

urlpatterns = [
   url('',include(router.urls)),
]