from rest_framework import viewsets, permissions
from .models import Family
from .serializers import FamilySerializer


class FamilyViewset(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [
        permissions.AllowAny
    ]
