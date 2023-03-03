from django.urls import include, path
from rest_framework import routers

from api.views import BasketSerializer, ProductModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BasketSerializer)

urlpatterns = [
    path('', include(router.urls)),
]
