from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="dashboard"),
    path('staff/',views.staff, name="staff"),
    path('product/',views.product, name="product"),
    path('order/',views.order, name="order")
]