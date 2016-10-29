from rest_framework import permissions

class IsAccountOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.account == request.user
