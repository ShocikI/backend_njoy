from rest_framework import permissions
from django.shortcuts import get_object_or_404

from njoy_backend.models import Event

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        username = view.kwargs.get('username_username')
        return (
            request.user.is_authenticated 
            and username == request.user.username
        )
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsEventOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        event_pk = view.kwargs.get('event_pk')
        if not event_pk:
            return False

        event = get_object_or_404(Event, pk=event_pk)
        return request.user.is_authenticated and event.owner == request.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.owner == request.user