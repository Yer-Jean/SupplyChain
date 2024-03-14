from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import ProductViewSet


app_name = MainConfig.name

router_product = DefaultRouter()
router_product.register('product', ProductViewSet, basename='product')

urlpatterns = [
    # path('', include(router.urls)),
    # path('', include(router_network.urls)),
    path('', include(router_product.urls)),
]

