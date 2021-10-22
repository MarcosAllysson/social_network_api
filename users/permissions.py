from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'DELETE' or request.method == 'GET' or request.method == 'POST' or request.method == 'PUT':

            if request.user.is_superuser:
                return True

            return False

        return True
