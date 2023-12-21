from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from restaurant.serializer import *
from restaurant.models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
class MenuItemSingleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
class BookingView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class BookingSingleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()