from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from food.models import FoodItem
from orders.models import Order
from .serializers import FoodSerializer, OrderSerializer

# Get all food items
@api_view(['GET'])
def food_list(request):
    foods = FoodItem.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Create order
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)