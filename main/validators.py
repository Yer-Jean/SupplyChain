from rest_framework import serializers


class SupplyNodeValidator:
    """ Проверяем, что категория поставщика не "Factory" и его уровень не равен 0 """

    def __call__(self, data):
        category = data.get('category')
        tier = data.get('tier')

        if category == 'FCT' or tier == 0:
            raise serializers.ValidationError("Нельзя добавить поставщика или задолженность "
                                              "для завода или поставщика с уровнем 0.")
