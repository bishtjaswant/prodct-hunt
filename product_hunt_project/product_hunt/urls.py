from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('accounts/', include("accounts.urls")),
    path('products/', include("products.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
