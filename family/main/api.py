from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Family, Assessment
from .serializers import FamilySerializer, AssessmentSerializer


class FamilyViewset(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ListAssessmentsByTarget(ListAPIView):
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        # target_pk = self.kwargs['target_pk']
        return Assessment.objects.all()
