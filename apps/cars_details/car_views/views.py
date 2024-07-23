from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.cars_details.car_views.models import CarViewModel
from apps.cars_details.car_views.serializers import CarViewsSerializer


class CarAdView(ListCreateAPIView):
    serializer_class = CarViewsSerializer
    queryset = CarViewModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (AllowAny(),)
        return (IsAuthenticated(),)

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car_view = CarViewModel.objects.get(car_ad_id=pk)
            car_view.views += 1
            car_view.save()
            serializer = CarViewsSerializer(car_view)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response({'message': 'Added'}, status=status.HTTP_200_OK)
        except CarViewModel.DoesNotExist:
            car_view = CarViewModel.objects.create(car_ad_id=pk, views=1)
            serializer = CarViewsSerializer(car_view, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response({'message': 'Created'}, status=status.HTTP_201_CREATED)


class CarAdListView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarViewsSerializer
    queryset = CarViewModel.objects.all()

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        exist = CarViewModel.objects.filter(pk=pk).exists()
        if not exist:
            raise Http404()
        views = CarViewModel.objects.filter(car_ad_id=pk)
        serializer = CarViewsSerializer(views, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
