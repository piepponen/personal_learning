from rest_framework import serializers
from decimal import Decimal
from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User, Group


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]


class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "featured", "category", "category_id"]
        extra_kwargs = {
            "price": {"min_value": 0},
        }
        

class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source="user.username")
    menuitem = serializers.StringRelatedField()
    menuitem_id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source="menuitem.price", read_only=True)
    subtotal = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ["id", "user", "menuitem_id", "menuitem", "quantity", "price", "subtotal"]
        read_only_fields = ["user", "menuitem", "price", "subtotal"]
        extra_kwargs = {
            "quantity": {"min_value": 1},
        }
        
    def get_subtotal(self, cart:Cart):
        subtotal = round(cart.menuitem.price * cart.quantity, 2)
        return f"{subtotal:.2f}"
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"  
        read_only_fields = ["user", "total", "date"]
        

class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = serializers.StringRelatedField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source="menuitem.price", read_only=True)
    subtotal = serializers.SerializerMethodField()
    status = serializers.StringRelatedField(source="order.status")
    delivery_crew = serializers.StringRelatedField(source="order.delivery_crew")
    
    class Meta:
        model = OrderItem
        fields = ["id", "order", "menuitem_id", "menuitem", "quantity", "price", "subtotal", "status", "delivery_crew"]
        read_only_fields = ["order", "menuitem_id", "menuitem", "total", "price", "subtotal"]
        
    def get_subtotal(self, order:OrderItem):
        subtotal = round(order.menuitem.price * order.quantity, 2)
        return f"{subtotal:.2f}"

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "date_joined", "is_active", "is_staff"]
        # exclude = ["password", "user_permissions"]
        read_only_fields = ["first_name", "last_name", "email", "date_joined", "is_active", "is_staff"]
        # depth = 1