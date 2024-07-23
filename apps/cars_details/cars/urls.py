from django.urls import path

from .views import AddPhotosToCarView, CarListView, CarRetrieveUpdateDestroyView, DeleteCarPhotoByIdOfPhotoView

urlpatterns = [
    path('', CarListView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/add_photos', AddPhotosToCarView.as_view()),
    path('/<int:pk>/delete_photo', DeleteCarPhotoByIdOfPhotoView.as_view()),

]
