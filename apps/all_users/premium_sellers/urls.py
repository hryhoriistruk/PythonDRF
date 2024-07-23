from django.urls import path

from .views import (  # get_view_counts,; PremiumSellerStatisticListView,; CorrectionAttemptView,
    PremiumSellerCarsListCreateView,
    PremiumSellerListView,
    PremiumSellerView,
)

# AveragePriceByRegionView,PremiumSellerDetailView,PremiumSellerListAndCarsView,
# # (  # PremiumSellerCarsListCreateView,; PremiumSellerCarsUpdateRetrieveDestroyListView,; PremiumSellersListCreateView,; PremiumSellerUpdateRetrieveDestroyListView,; PremiumSellerCarsListCreateView,
# #    ,
# # )
#
# #




urlpatterns = [
    path('', PremiumSellerListView.as_view()),
    path('/<int:pk>', PremiumSellerView.as_view()),
    # path('/car_views/<int:user_id>', get_view_counts),
    # path('/<int:pk>/statistics', PremiumSellerStatisticListView.as_view()),
    # path('/<int:pk>', PremiumSellerListAndCarsView.as_view()),
    # path('/<int:pk>', PremiumSellerDetailView.as_view()),
    path('/<int:pk>/cars', PremiumSellerCarsListCreateView.as_view()),
    # path('/<int:pk>/desciptions', CorrectionAttemptView.as_view())
    # path('/<int:pk>/cars/average_price', AveragePriceByRegionView.as_view()), #
    #     path('/<int:pk>/cars/<int:cars>', PremiumSellerCarsDetailView.as_view()) #перевірити чи працює!!!!
]
