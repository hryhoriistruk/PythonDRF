from django.urls import path

from .views import ChangeSellerToPremiumSellerView, SellerCarsListCreateView, SellerListByIdView, SellerListView

# SellerAddCarView,
# SellersListCreateView, SellerListUpdateRetrieveDestroyView,
# )
urlpatterns = [
    path('', SellerListView.as_view()),
    path('/<int:pk>', SellerListByIdView.as_view()),
    path('/<int:pk>/cars', SellerCarsListCreateView.as_view()),
    path('/<int:pk>/to_premium_seller', ChangeSellerToPremiumSellerView.as_view())
    # path('/<int:pk>', SellerListUpdateRetrieveDestroyView.as_view()),
    # path('/<int:pk>/cars', SellerCarsListCreateView.as_view())
]
