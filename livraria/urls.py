from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from core.views import CategoriaViewSet
from core.views import EditoraViewSet
from core.views import AutorViewSet
from core.views import LivroViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]
