from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from core.models import Autor 
from core.models import Editora

from core.serializers import CategoriaSerializer
from core.serializers import AutorSerializer
from core.serializers import EditorasSerializer


class AutorViwSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditorasViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditorasSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer