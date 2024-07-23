# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.serializers import ValidationError
#
# from .models import CarModel


from django_filters import rest_framework as filters

from .choices.body_type_choices import BodyTypeChoices
# from .choices.brand_choices import BrandChoices
from .choices.engine_types_choises import EngineTypesChoices
from .choices.transmission_types_choices import TransmissionTypeChoices


class CarFilter(filters.FilterSet):
    pass
    # brand_icontains = filters.CharFilter('brand_models', 'icontains')
    # brand_istartswith = filters.CharFilter('brand_models', 'istartswith')
    # # brand_models = filters.ChoiceFilter('brand_models', choices=BrandChoices.choices)
    # model_icontains = filters.CharFilter('model', 'icontains')
    # model_istartswith = filters.CharFilter('model', 'istartswith')
    # color_istartswith = filters.CharFilter('color', 'istartswith')
    # body_type_choice = filters.ChoiceFilter(BodyTypeChoices.choices)
    # year_range = filters.RangeFilter('year')
    # year_in = filters.BaseInFilter('year')
    # price_range = filters.RangeFilter('price')
    # seat_count = filters.NumberFilter('seat_count')
    # body_type = filters.CharFilter('body_type', 'istartswith')
    # engine_type = filters.CharFilter('engine_type', 'istartswith')
    # engine_type_choice = filters.ChoiceFilter(EngineTypesChoices.choices)
    # engine_volume_range = filters.RangeFilter('engine_volume')
    # transmission = filters.CharFilter('transmission', 'istartswith')
    # transmission_choice = filters.ChoiceFilter(TransmissionTypeChoices)
    # mileage_range = filters.RangeFilter('mileage')
    # region = filters.CharFilter('region', 'istartswith')
    # order = filters.OrderingFilter(
    #     fields=(
    #         'brand_models',
    #         'year',
    #         'price',
    #         'mileage',
    #         'created_at'
    #     )
    # )
