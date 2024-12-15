from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    IsAdminUser
)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Manager").exists()


class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Delivery Crew").exists()
    
    
class IsDeliveryCrewAndOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Delivery Crew").exists()

    def has_object_permission(self, request, view, obj):
        return obj.delivery_crew == request.user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        # return (request.method in SAFE_METHODS) and request.user.is_authenticated
        return request.method in SAFE_METHODS
    

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        # The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed
        return request.user.is_authenticated and (not request.user.is_staff)
        # user, not belonging to any group = Customer
        # return request.user.is_authenticated and self.request.user.groups.count() == 0


class IsCustomerAndOwner(BasePermission):
    def has_permission(self, request, view):
        # The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed
        return request.user.is_authenticated and (not request.user.is_staff)
        # user, not belonging to any group = Customer
        # return request.user.is_authenticated and self.request.user.groups.count() == 0
        
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
