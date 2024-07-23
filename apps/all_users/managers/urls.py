from django.urls import path

#
from .views import BanUserView, UnBanUserView

# CreateManagersListView, ManagersListUpdateRetrieveDestroyView

urlpatterns = [
    path('/<int:pk>/ban_user', BanUserView.as_view()),
    path('<int:pk>/un_ban_user', UnBanUserView.as_view())
    #     path('', CreateManagersListView.as_view()),
    #     path('/<int:pk>', ManagersListUpdateRetrieveDestroyView.as_view())
]
