from django.contrib import admin
from django.urls import path, include
from qualityapp.views import inspector_fpy_view  # 👈 IMPORTAMOS LA VISTA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloapp.urls')),           # si aún la usas
    path('quality/', include('qualityapp.urls')),       # ruta normal
    path('', inspector_fpy_view, name='home'),          # 👈 RUTA RAÍZ
]