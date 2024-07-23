from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Info
from .serializers import InfoSerializer


class InfoView(ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (IsAdminUser,)

    def get_permissions(self):
        if self.request.method == 'POST':
            return (IsAdminUser(),)
        return (AllowAny(),)
