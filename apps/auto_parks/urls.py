from django.urls import include, path

from .views import AutoParkCarListCreateView, AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view()),
]
