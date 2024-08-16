from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


def index(request):
    return render(request, "restaurant/index.html", {})


class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
