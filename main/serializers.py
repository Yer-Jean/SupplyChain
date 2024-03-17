from rest_framework import serializers

from main.models import Product, SupplyNode, Contact


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


# class ContactListSerializer(serializers.ModelSerializer):
#     supply_node_addresses = serializers.SerializerMethodField()
#     supply_node_name = serializers.CharField(source='supply_node.name', read_only=True)
#
#     class Meta:
#         model = Contact
#         fields = ('supply_node_name', 'supply_node_addresses',)
#
#     def get_supply_node_addresses(self, supply_node):
#         return ContactSerializer(Contact.objects.filter(id=supply_node.id), many=True).data
#
#     def get_supply_node_name(self, obj):
#         return obj.supply_node.name


class SupplyNodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplyNode
        fields = '__all__'


class SupplyNodeListViewSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display', read_only=True)
    addresses = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SupplyNode
        fields = ('name', 'category', 'supplier_tier', 'debt', 'tier', 'addresses', 'products',)

    def get_addresses(self, obj):
        contacts = obj.contact_set.all()
        return ContactSerializer(contacts, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation
