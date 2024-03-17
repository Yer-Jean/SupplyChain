from rest_framework import serializers

from main.models import Product, SupplyNode, Contact
from main.validators import SupplyNodeValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactListDetailSerializer(serializers.ModelSerializer):
    # Выводим наименование поставщика, а не его ID
    supply_node_name = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        exclude = ('supply_node',)

    def get_supply_node_name(self, obj):
        return obj.supply_node.name if obj.supply_node else None


class SupplyNodeSerializer(serializers.ModelSerializer):
    validators = [SupplyNodeValidator(),]

    class Meta:
        model = SupplyNode
        fields = '__all__'


class SupplyNodeUpdateSerializer(serializers.ModelSerializer):
    validators = [SupplyNodeValidator(),]

    class Meta:
        model = SupplyNode
        fields = '__all__'

    def validate(self, attrs):
        # Проверяем, что поле debt не было включено в данные запроса
        if 'debt' in attrs:
            raise serializers.ValidationError("Обновление поля 'Задолженность' запрещено.")
        return attrs


class SupplyNodeListViewSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display', read_only=True)
    addresses = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SupplyNode
        fields = ('id', 'name', 'category', 'supplier_tier', 'debt', 'tier', 'addresses', 'products',)

    def get_addresses(self, obj):
        contacts = obj.contact_set.all()
        return ContactSerializer(contacts, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation
