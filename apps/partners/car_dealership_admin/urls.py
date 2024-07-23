from django.urls import path

from .views import AdminDealershipListCreateView

urlpatterns = [
    path('', AdminDealershipListCreateView.as_view())
]
