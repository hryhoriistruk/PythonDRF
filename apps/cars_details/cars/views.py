from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

# from .filters import car_filtered_queryset
# from .filters import CarFilter
from .models import CarModelV2, CarPhotosModel
from .serializers import CarPhotosListSerializer, CarSerializer

# from requests import Response


# from rest_framework.response import Response


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModelV2.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return (IsAuthenticated(),)
    # filterset_class = CarFilter # не працюють фільтри тому що в моделях майже всі поля закоментовані


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModelV2.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return (IsAuthenticated(),)


# class AddPhotosToCarView(ListCreateAPIView):
# serializer_class = CarPhotosListSerializer
# queryset = CarPhotosModel.objects.all()

class AddPhotosToCarView(GenericAPIView):
    serializer_class = CarPhotosListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context |= {'car': self.request.image.car}
        return context
        # return self.request

    # def post(self, *args, **kwargs):
    #     serializer = self.get_serializer(data=self.request.FILES)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     print(serializer.data)
    #     return Response('ok')
    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModelV2.objects.get(pk=pk)
        except CarModelV2.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        images_data = self.request.FILES.getlist('image')
        if not images_data:
            return Response({"error": "No photos provided"}, status=status.HTTP_400_BAD_REQUEST)

        for image in images_data:
            CarPhotosModel.objects.create(car=car, image=image)

        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def get(self, *args, **kwargs):
    #     qs = CarPhotosModel.objects.all().filter(car_id=self.get_object().id)
    #     serializer = self.serializer_class(qs, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

# class AddPhotosToCarView(CreateAPIView):
# class AddPhotosToCarView(CreateAPIView):
#     serializer_class = CarPhotosListSerializer
#     queryset = CarModel.objects.all()
#     #
# def patch(self, *args, **kwargs):
#     car = self.get_object()
#     photos = self.request.FILES
#     for photo in photos:
#         serializer = self.serializer_class(data={'photos': photos[photo]})
#         serializer.is_valid(raise_exception=True)
#         serializer.save(car=car)
#     serializer = CarSerializer(car)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# def get(self, *args, **kwargs):
#     qs = CarPhotosModel.objects.all().filter(car_id=self.get_object().id)
#     serializer = self.serializer_class(qs, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

######################################################################################################################
# ПЕРЕВІРИТИ НА ДОДАВАННЯ БАГАТЬОХ ФОТОГРАФІЙ ОДНОЧАСНО

# def get_serializer_context(self):
#     # context = super().get_serializer_context()
#     # print(context)
#     return (self.request.data)
# context |= {'car': self.request.car}
# return context
###################################################################################################################

# queryset = CarModel.objects.all()
# serializer_class = CarSerializer
#
# def post(self, *args, **kwargs):
#     car = self.get_object()
#     files = self.request.FILES
#     for key in files:
#         serializer = CarPhotosListSerializer(data={'photos': files[key]})
#         serializer.is_valid(raise_exception=True)
#         serializer.save(car=car)
#     serializer = self.serializer_class(car)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

# def post(self, *args, **kwargs):
#     serializer = CarPhotosListSerializer(data=self.request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response('ok', status=status.HTTP_201_CREATED)

# serializer_class = CarPhotosListSerializer
#
# def get_serializer_context(self):
#     context = super().get_serializer_context()
#     context |= {'car': self.request} #?
#     return context
#
# def post(self, *args, **kwargs):
#     serializer = self.get_serializer(data=self.request.FILES)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     print(serializer.data)
#     return Response('ok')

# def patch(self, *args, **kwargs):
#     car = self.get_object()
#     files = self.request.FILES
#     for key in files:
#         serializer = self.serializer_class(data={'photos': files[key]})
#         serializer.is_valid(raise_exception=True)
#         serializer.save(car=car)
#     serializer = CarSerializer(car)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
# def put(self, *args, **kwargs):
#     serializer = CarPhotosSerializer(self.request, data=self.request.FILES, context={'request': self.request})
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def get(self, *args, **kwargs):
#     qs = CarPhotosModel.objects.all().filter(car_id=self.get_object().id)
#     serializer = self.serializer_class(qs, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# class AddPhotosToCarView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def post(self, *args, **kwargs):
#         car = self.get_object()
#         # print(car)
#         files = self.request.FILES
#         for key in files:
#             serializer = CarPhotosListSerializer(data={'photo': files[key]})
#             serializer.is_valid(raise_exception=True)
#             serializer.save(car=car)
#         serializer = self.serializer_class(car)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
class DeleteCarPhotoByIdOfPhotoView(DestroyAPIView):
    serializer_class = CarPhotosListSerializer
    queryset = CarPhotosModel.objects.all()
