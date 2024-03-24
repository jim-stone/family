from rest_framework.permissions import BasePermission
# from .models import User
# from .serializers import UserSerializer


class IsWishOwnerUserOrWishHasNoOwnerUser(BasePermission):

    message = 'Nie możesz wykonać tej akcji za innego użytkownika'

    def has_permission(self, request, view):
        userId = request.user.id
        print(request.data)
        if view.action == 'create':
            wishUserId = request.data.get('owner_user')
            condition1 = str(userId) == str(wishUserId)
            condition2 = wishUserId is None
            return condition1 or condition2
        if view.action == 'partial_update':
            wishUserId = request.data.get('ownerUser')
            condition1 = str(userId) == str(wishUserId)
            condition2 = wishUserId is None
            if request.data.get('status') == 2:
                return True
            if request.data.get('status') in (3, 4):
                return condition1 or condition2


def family_member_filter(request):
    family_ids = [m.family.id for m in request.user.members.all()]
    return family_ids
