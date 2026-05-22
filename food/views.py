from django.shortcuts import render, redirect
from .models import FoodItem
from orders.models import Order

def menu_view(request):
    foods = FoodItem.objects.all().order_by("name")

    categories = (
        FoodItem.objects.values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )

    return render(request, "menu.html", {
        "foods": foods,
        "categories": categories
    })


def add_to_cart(request, food_id):
    cart = request.session.get("cart", {})
    food_id = str(food_id)

    cart[food_id] = cart.get(food_id, 0) + 1
    request.session["cart"] = cart
    return redirect("/")


def remove_from_cart(request, food_id):
    cart = request.session.get("cart", {})
    food_id = str(food_id)

    if food_id in cart:
        del cart[food_id]

    request.session["cart"] = cart
    return redirect("/cart/")


def cart_view(request):
    cart = request.session.get("cart", {})
    items = []
    total = 0

    for food_id, qty in cart.items():
        food = FoodItem.objects.get(id=int(food_id))
        subtotal = food.price * qty
        total += subtotal
        items.append({"food": food, "qty": qty, "subtotal": subtotal})

    return render(request, "cart.html", {"items": items, "total": total})


def place_order(request):
    cart = request.session.get("cart", {})

    if request.method == "POST":
        name = request.POST.get("customer_name")
        address = request.POST.get("address")

        for food_id, qty in cart.items():
            food = FoodItem.objects.get(id=int(food_id))
            Order.objects.create(
                customer_name=name,
                food_item=food,
                quantity=qty,
                address=address
            )

        request.session["cart"] = {}
        return render(request, "order_success.html")

    return render(request, "checkout.html")