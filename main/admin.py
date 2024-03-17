from django.contrib import admin

from main.models import SupplyNode, Product, Contact


@admin.register(SupplyNode)
class SupplyNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier_tier', 'debt', 'tier', 'created_date',)
    filter_horizontal = ('products',)
    # list_filter = ('title',)
    actions = ('clear_debt',)

    def clear_debt(self, request, queryset):
        pass

    clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'launch_date',)
    # list_filter = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('supply_node', 'email', 'country',)
    # list_filter = ('title',)
