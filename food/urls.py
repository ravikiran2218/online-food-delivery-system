from django.urls import path
from .views import menu_view, add_to_cart, cart_view, place_order, remove_from_cart

urlpatterns = [
    path("", menu_view, name="menu"),
    path("add/<int:food_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:food_id>/", remove_from_cart, name="remove_from_cart"),
    path("cart/", cart_view, name="cart"),
    path("checkout/", place_order, name="checkout"),
]