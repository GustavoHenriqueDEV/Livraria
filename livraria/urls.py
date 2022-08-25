from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from core.views import CategoriaViewSet
from core.views import EditorasViewSet
from core.views import AutorViwSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditorasViewSet)
router.register(r'autor', AutorViwSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

