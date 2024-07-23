from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import AdminCarDealershipSerializer
from .models import AdminCarDealershipModel


class AdminDealershipListCreateView(GenericAPIView):
    def get(self, *args, **kwargs):
        query_set = AdminCarDealershipModel.objects.all()
        serializer = AdminCarDealershipSerializer(query_set, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AdminCarDealershipSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)