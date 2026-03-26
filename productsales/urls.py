from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('product/', include('products.urls')),
    path('auth/', include('authentication.urls')),
    path('', RedirectView.as_view(url='/products/', permanent=True))
]