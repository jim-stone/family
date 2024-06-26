from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, status, views
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from .models import Family, Assessment, Member, Wish
from .serializers import (
    FamilySerializer, AssessmentSerializer, AssessmentCreateSerializer,
    LoginSerializer, UserSerializer, WishReadSerializer, WishWriteSerializer
)
from .custom_permissions import family_member_filter, IsWishOwnerUserOrWishHasNoOwnerUser


class WishWriteViewset (viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishWriteSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsWishOwnerUserOrWishHasNoOwnerUser
    ]

    def create(self, request):
        serializer = WishWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # response = Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'status_code': 201})

    @action(detail=False, methods=['PATCH'], url_path='wishes_write/(?P<wish_id>[^/.]+)')
    def change_wish_status(self, request, wish_id=None):
        wish = Member.objects.get(pk=wish_id)
        serializer = self.get_serializer(wish, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response({'status_code': 200})


class WishReadViewset (viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishReadSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @action(detail=False, methods=['get'], url_path='member/(?P<member_id>[^/.]+)')
    def wishes_of_a_member(self, request, member_id=None):
        member = Member.objects.get(pk=member_id)
        if member.is_user:
            result = Wish.objects.filter(owner_user__id=member.user.id)
        else:
            result = Wish.objects.filter(owner_member__id=member_id)
        serializer = WishReadSerializer(result, many=True)
        return Response(serializer.data)


class FamilyViewset(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def list(self, request):
        user_families = family_member_filter(request)
        queryset = Family.objects.filter(id__in=user_families)
        serializer = FamilySerializer(queryset, many=True)
        return Response(serializer.data)


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
        return Response(f'User logged in: {user.username}', status=status.HTTP_202_ACCEPTED)


class LogoutView (views.APIView):
    def post(self, request):
        logout(request)
        return redirect('/index/')


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_data = {}
            user_data.update(serializer.data)
            user_data.update(
                {'password': request.data['password']}
            )
            print(user_data)
            User.objects.create_user(**user_data)
        except Exception as e:
            print(e)
            return Response(serializer.errors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
