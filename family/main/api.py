from django.contrib.auth import login, logout
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, status, views
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from .models import Family, Assessment, Member
from .serializers import FamilySerializer, AssessmentSerializer, AssessmentCreateSerializer, LoginSerializer


class FamilyViewset(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [
        permissions.AllowAny
    ]


class AsessmentViewset(viewsets.ViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentCreateSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def list(self, request):
        serializer = AssessmentSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AssessmentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        family_id = serializer.validated_data['member_target'].family_id
        user_id = request.user.id
        if user_id:
            member_source = Member.objects.get(user=user_id, family=family_id)
            serializer.validated_data['member_source'] = member_source
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['get'], url_path='about_member/(?P<member_id>[^/.]+)')
    def about_member(self, request, member_id=None):

        result = Assessment.objects.filter(member_target_id=member_id)
        serializer = AssessmentSerializer(result, many=True)
        return Response(serializer.data)


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class LogoutView (views.APIView):
    def post(self, request):
        logout(request)
        return redirect('/index/')
