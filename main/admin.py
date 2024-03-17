from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from main.models import SupplyNode, Product, Contact


@admin.register(SupplyNode)
class SupplyNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier_tier_link', 'debt', 'tier', 'created_date',)
    filter_horizontal = ('products',)
    # 'contact__city' - добавляет фильтр по городу в админ-панель Django
    list_filter = ('category', 'supplier_tier', 'contact__city',)
    actions = ('clear_debt',)

    def clear_debt(self, request, queryset):
        """ Метод очищает задолженность перед поставщиком для выбранных
        торговых узлов сети в админ-панели Django"""
        for supply_node in queryset:
            supply_node.debt = 0
            supply_node.save()
        self.message_user(request, f'Задолженность перед поставщиком удалена.')
    clear_debt.short_description = "Удалить задолженность перед поставщиком"

    def supplier_tier_link(self, obj):
        """ Метод показывает в табличной части админ-панели Django поставщика,
        как ссылку на него в этой же админ-панели """
        if obj.supplier_tier:
            link = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),
                           args=[obj.supplier_tier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier_tier.name)
        else:
            return "None"
    supplier_tier_link.short_description = "Поставщик"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'launch_date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('supply_node', 'email', 'country',)
