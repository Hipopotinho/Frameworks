from django.contrib import admin
from accounts.models.cep import Cep

@admin.register(Cep)
class CepAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'logradouro')
    list_select_related = ('logradouro',)
    search_fields = ('codigo',)