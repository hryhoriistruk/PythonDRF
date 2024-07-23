from django.urls import path

from .views import BanManagerView, ManagerToUserView, UnBanManagerView, UserToManagerView

urlpatterns = [
    path('/<int:pk>/user_to_manager', UserToManagerView.as_view()),
    path('/<int:pk>/manager_to_user', ManagerToUserView.as_view()),
    path('/<int:pk>/ban_manager', BanManagerView.as_view()),
    path('/<int:pk>/un_ban_manager', UnBanManagerView.as_view())
]

