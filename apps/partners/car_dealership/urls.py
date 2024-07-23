from django.urls import path

from .views import CarDealershipCarsListCreateView

urlpatterns = [
    path('', CarDealershipCarsListCreateView.as_view())
]
