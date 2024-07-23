from django.urls import path

from .views import VisitorsCreateListView, VisitorsUpdateRetrieveDestroyListView

urlpatterns = [
    path('', VisitorsCreateListView.as_view()),
    path('/<int:pk>', VisitorsUpdateRetrieveDestroyListView.as_view())
]
