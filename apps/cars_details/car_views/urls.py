from django.urls import path

from .views import CarAdListView, CarAdView

urlpatterns = [
    path('/<int:pk>', CarAdView.as_view()),
    path('/<int:pk>/views', CarAdListView.as_view())
]
