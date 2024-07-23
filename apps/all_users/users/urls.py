from django.urls import path

from .views import (  # UsersListView; UpdateUserProfileView,
    AddAvatarToProfileView,
    OwnerAccountListView,
    TestEmailView,
    UserListCreateView,
    UserListRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', UserListCreateView.as_view()), #works
    path('/email', TestEmailView.as_view()),
    # path('/see_all', UsersListView.as_view()),
    path('/<int:pk>', UserListRetrieveUpdateDestroyView.as_view()), #works
    path('/<int:pk>/add_avatar', AddAvatarToProfileView.as_view()), #works
    path('/<int:pk>/create_account', OwnerAccountListView.as_view()),

    # path('/update/<int:pk>', UpdateUserProfileView.as_view())
    # path('/<int:pk>/cars', SellerCarsListCreateView.as_view())
    # path('/my', MyView.as_view()),
    # path('/roles', RolesCreateAPIView.as_view())
    # path('/add_sellers', SellerListCreateView.as_view())
]

