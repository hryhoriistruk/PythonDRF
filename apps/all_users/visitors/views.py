from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import VisitorSerializer
from .models import VisitorModel


class VisitorsCreateListView(ListCreateAPIView):
    serializer_class = VisitorSerializer
    queryset = VisitorModel.objects.all()


class VisitorsUpdateRetrieveDestroyListView(RetrieveUpdateDestroyAPIView):
    serializer_class = VisitorSerializer
    queryset = VisitorModel.objects.all()