from rest_framework.serializers import ModelSerializer

from core.models import Categoria
from core.models import Editora
from core.models import Autor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor 
        fields = "__all__"

class EditorasSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
        
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

