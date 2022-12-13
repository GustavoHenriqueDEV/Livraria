from rest_framework.viewsets import ModelViewSet

from core.models import Autor, Categoria, Editora, Livro
from core.serializers import (
    AutorSerializer,
    CategoriaSerializer,
    EditoraSerializer,
    LivroSerializer,
)


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorViwSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class EditorasViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_clas = LivroSerializer
