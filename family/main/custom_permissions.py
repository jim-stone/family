# from rest_framework.permissions import BasePermission
# from .models import User
# from .serializers import UserSerializer


# class IsFamilyMember(BasePermission):
#     def has_permission(self, request, view):
#         family_ids = [m.family.id for m in request.user.members.all()]
#         print(family_ids)
#         return True


def family_member_filter(request):
    family_ids = [m.family.id for m in request.user.members.all()]
    return family_ids
