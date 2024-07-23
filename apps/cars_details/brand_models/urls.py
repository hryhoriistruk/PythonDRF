from django.urls import path

from .views import (  # CurrencyConverter,
    CarsBrandListCreateView,
    CarsBrandListUpdateRetrieveDestroyView,
    CarsModelListCreateView,
    CarsModelListUpdateRetrieveDestroyView,
)

urlpatterns = [
    path('', CarsBrandListCreateView.as_view()),
    path('/<str:brand>', CarsBrandListUpdateRetrieveDestroyView.as_view()),
    path('/<str:brand>/model', CarsModelListCreateView.as_view()),
    # path('brand_models/<str:brand_models>/<str:model>', CarsModelListCreateView.as_view()),
    # path('/currency', CurrencyConverter.as_view())
    # path('/<str:brand_models>/<str:model>', CarsModelListCreateView.as_view()),
    # path('/<str:brand_models>/<str:model>', CarsModelListUpdateRetrieveDestroyView.as_view())
]
