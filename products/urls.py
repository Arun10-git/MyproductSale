from django.urls import path
from .views import *

urlpatterns = [
    path('carts/', cartbyview.as_view()),
    path('carts/<int:id>/', cartbyview.as_view()),
    path('', productforsales.as_view()),
    path('<int:prod_id>/', productforsalesbyid.as_view())
]