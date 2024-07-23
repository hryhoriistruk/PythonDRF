from django.urls import path

from .views import UserListCreateView, BlockUserView, UnBlockUserView, UserToAdminView, AdminToUserView, \
    BlockAdminUserView, UnBlockAdminUserView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/user_to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/admin_to_user', AdminToUserView.as_view()),
    path('/<int:pk>/block_user', BlockUserView.as_view()),
    path('/<int:pk>/un_block_user', UnBlockUserView.as_view()),
    path('/<int:pk>/un_block_user', UnBlockUserView.as_view()),
    path('/<int:pk>/block_admin', BlockAdminUserView.as_view()),
    path('/<int:pk>/un_block_admin', UnBlockAdminUserView.as_view()),
]
