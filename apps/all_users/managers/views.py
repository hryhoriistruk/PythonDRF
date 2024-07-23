from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from core.permission.is_super_user import IsSuperUser

from apps.all_users.users.serializers import UserSerializer


#
# from .models import ManagerModel
# from .serializers import ManagerSerializer
#
class NotifyManager(GenericAPIView):
    def post(self, request, *args, **kwargs):
        brand_name = request.data.get('brand_name')
        # write code how to send email to manager
        return Response("Manager has been notified", status=status.HTTP_200_OK)


#
# class CreateManagersListView(ListCreateAPIView):
#     serializer_class = ManagerSerializer
#     queryset = ManagerModel.objects.all()
#
#
# class ManagersListUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
#     serializer_class = ManagerSerializer
#     queryset = ManagerModel.objects.all()
from rest_framework.permissions import IsAdminUser


class BanUserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBanUserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
