from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Livro


class LivroSerializer(ModelSerializer):

    class Meta:
        model = Livro
        fields = "__all__"
