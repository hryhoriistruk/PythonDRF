from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MeView, ActivateUserView, RecoveryPasswordView, RecoveryPasswordRequestView
urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/recovery_password', RecoveryPasswordRequestView.as_view()),
    path('/recovery_password/<str:token>', RecoveryPasswordView.as_view()),
    path('/me', MeView.as_view()),
]