from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView

from main.models import Product, SupplyNode, Contact
from main.permissions import IsActive
from main.serializers import ProductSerializer, SupplyNodeSerializer, ContactSerializer, ContactListDetailSerializer, \
    SupplyNodeListViewSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActive]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [IsActive]

    default_serializer = ContactSerializer
    ListSerializers = {
        'list': ContactListDetailSerializer,
        'retrieve': ContactListDetailSerializer,
    }

    def get_serializer_class(self):
        # Ищет в словаре ListSerializers - action. Если находит, то использует
        # соответствующий сериалайзер, если не находит, то используется дефолтный
        return self.ListSerializers.get(self.action, self.default_serializer)


class SupplyNodeCreateAPIView(CreateAPIView):
    serializer_class = SupplyNodeSerializer
    permission_classes = [IsActive]


class SupplyNodeViewAPIView(RetrieveAPIView):
    serializer_class = SupplyNodeListViewSerializer
    queryset = SupplyNode.objects.all()
    permission_classes = [IsActive]


class SupplyNodeListAPIView(ListAPIView):
    serializer_class = SupplyNodeListViewSerializer
    queryset = SupplyNode.objects.all()
    permission_classes = [IsActive]


class SupplyNodeUpdateAPIView(UpdateAPIView):
    serializer_class = SupplyNodeSerializer
    queryset = SupplyNode.objects.all()
    permission_classes = [IsActive]


class SupplyNodeDeleteAPIView(DestroyAPIView):
    serializer_class = SupplyNodeSerializer
    queryset = SupplyNode.objects.all()
    permission_classes = [IsActive]
