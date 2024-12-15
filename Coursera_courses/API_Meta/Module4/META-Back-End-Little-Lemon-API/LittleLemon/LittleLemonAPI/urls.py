from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
router.register("category", views.CategoryViewSet, basename="category")
router.register("menu-items", views.MenuItemViewSet, basename="menu-items")


urlpatterns = [
    path("", include(router.urls)),
    path("groups/manager/users", views.ManagerPostView.as_view(), name="manager"),
    path("groups/manager/users/<int:pk>", views.ManagerDeleteView.as_view(), name="manager-detail"),
    path("groups/delivery-crew/users", views.DeliveryCrewPostView.as_view(),name="delivery-crew"),
    path("groups/delivery-crew/users/<int:pk>", views.DeliveryCrewDeleteView.as_view(), name="delivery-crew-detail"),
    path("cart/menu-items", views.CartView.as_view(), name="cart"),
    path("cart/menu-items/<int:pk>", views.CartItemView.as_view(), name="cart-detail"),
    path("orders", views.OrdersView.as_view(), name="orders"),
    path("orders/<int:pk>", views.OrderItemView.as_view(), name="orders-detail"),
]
