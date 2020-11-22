from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """Check if the user is owner of current object"""
        return obj.user == request.user


class CartIsNotInOrder(permissions.BasePermission):
    message = 'Cannot perform deleting Product. It is already in order'

    def has_object_permission(self, request, view, obj):
        """Check if product is in order"""
        return not obj.cart.in_order
