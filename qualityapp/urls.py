from django.urls import path
from .views import inspector_fpy_view

urlpatterns = [
    path("inspectores/", inspector_fpy_view, name="inspectors_fpy"),
]