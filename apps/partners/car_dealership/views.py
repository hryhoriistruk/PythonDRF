from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import CarDealerShipSerializer
from .models import CarDealershipModel


class CarDealershipCarsListCreateView(GenericAPIView):
    def get(self, *args, **kwargs):
        query_set = CarDealershipModel.objects.all()
        serializer = CarDealerShipSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarDealerShipSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)