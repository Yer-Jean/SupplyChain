from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import ProductViewSet, SupplyNodeCreateAPIView, SupplyNodeUpdateAPIView, ContactViewSet, \
    SupplyNodeViewAPIView, SupplyNodeListAPIView, SupplyNodeDeleteAPIView

app_name = MainConfig.name

router_product = DefaultRouter()
router_product.register('product', ProductViewSet, basename='product')
router_contact = DefaultRouter()
router_contact.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('node/', SupplyNodeListAPIView.as_view(), name='node_list'),
    path('node/create/', SupplyNodeCreateAPIView.as_view(), name='node_create'),
    path('node/update/<int:pk>/', SupplyNodeUpdateAPIView.as_view(), name='node_update'),
    path('node/view/<int:pk>/', SupplyNodeViewAPIView.as_view(), name='node_view'),
    path('node/delete/<int:pk>/', SupplyNodeDeleteAPIView.as_view(), name='node_delete'),

    path('', include(router_product.urls)),
    path('', include(router_contact.urls)),
]
