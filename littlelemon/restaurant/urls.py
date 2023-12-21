from django.urls import path
from restaurant.views import *
urlpatterns = [
     path('menu/items', MenuView.as_view()),
     path('booking/tables', BookingView.as_view()),
     path('menu/items/<int:pk>', MenuItemSingleView.as_view()),
     path('booking/tables/<int:pk>', BookingSingleView.as_view())
]
