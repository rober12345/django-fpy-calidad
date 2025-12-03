from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", include("helloapp.urls")),       # si aún lo usas
    path("quality/", include("qualityapp.urls")),   # << aquí vamos a entrar
]