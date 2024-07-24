# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.serializers import ValidationError
#
# from .models import CarModel
#
#
# def car_filtered_queryset(query: QueryDict) -> QuerySet:
#     qs = CarModel.objects.all()
#     query = query.dict()
#     query.pop('page', None)
#     query.pop('size', None)
#     for k, v in query.items():
#         match k:
#             case 'price_gt':
#                 qs = qs.filter(price__gt=v)
#             case 'price_gte':
#                 qs = qs.filter(price__gte=v)
#             case 'price_lt':
#                 qs = qs.filter(price__lt=v)
#             case 'price_lte':
#                 qs = qs.filter(price__lte=v)
#
#             case 'year_gt':
#                 qs = qs.filter(year__gt=v)
#             case 'year_gte':
#                 qs = qs.filter(year__gte=v)
#             case 'year_lt':
#                 qs = qs.filter(year__lt=v)
#             case 'year_lte':
#                 qs = qs.filter(year__lte=v)
#
#             case 'auto_park_id':
#                 qs = qs.filter(auto_park_id=v)
#
#             case 'brand_start_with':
#                 qs = qs.filter(brand__istartswith=v)
#             case 'brand_end_with':
#                 qs = qs.filter(brand__iendswith=v)
#             case 'brand_contains':
#                 qs = qs.filter(brand__icontains=v)
#
#             case 'order':
#                 qs = qs.order_by(v)
#             case _:
#                 raise ValidationError({'details': f'"{k}" not allowed here'})
#     return qs

from django_filters import rest_framework as filters

from apps.cars.models import CarModel

from .choices.body_types_choices import BodyTypeChoices


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', 'lt')
    year_gt = filters.NumberFilter('year', 'gt')
    year_range = filters.RangeFilter('year')
    year_in = filters.filters.BaseInFilter('year')
    brand_contains = filters.CharFilter('brand', 'icontains')
    body = filters.ChoiceFilter('body', choices=BodyTypeChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            'id',
            'brand',
            'year',
            'price'
        )
    )

    # class Meta:
    #     model = CarModel
    # fields = ('id', 'brand', 'year', 'price',)  # строга фільтрація brand=чомусь
    # fields = {
    #     'brand': ('istartswith', 'iendswith', 'icontains'),
    #     'year': ('gt', 'gte', 'lt', 'lte'),
    #     'price': ('gt', 'gte', 'lt', 'lte')
    # }
