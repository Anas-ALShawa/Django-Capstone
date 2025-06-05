from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def home(request):
    return render(request,"home.html")
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [IsAuthenticated]
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]