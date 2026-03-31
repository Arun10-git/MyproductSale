from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.generic import RedirectView

def home(request):
    return HttpResponse("My Product Sale App is Live 🚀")

urlpatterns = [
    path('', home), 
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('auth/', include('authentication.urls')),
]