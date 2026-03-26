from django.urls import path, include,admin
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('auth/', include('authentication.urls')),
    path('', RedirectView.as_view(url='/product/', permanent=True))
]