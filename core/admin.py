from django.contrib import admin
from core.models import Editora, Autor, Livro, Categoria
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
