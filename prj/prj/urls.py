"""
URL configuration for prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from main.views import vytvor_objednavku
from django.conf.urls.static import static
from main.views import zrusit_objednavku
from main.views import get_vkosiku
from main.views import (
    get_homepage,
    get_produkty,
    get_obednavky,
    get_vkosiku,
    produkty_list,
)

urlpatterns = [
    path('produkty/', produkty_list, name='produkty'),
    path('produkty/<int:id>/', get_produkty, name='produkt_detail'),
    path('admin/', admin.site.urls),
    path('', get_homepage, name='homepage'),
    path('vkosiku/', get_vkosiku, name='vkosiku'),
    path('obednavky/', get_obednavky, name='obednavky'),
    path('vytvor_objednavku/', vytvor_objednavku, name='vytvor_objednavku'),
    path('zrusit_objednavku/<int:objednavka_id>/', zrusit_objednavku, name='zrusit_objednavku'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
