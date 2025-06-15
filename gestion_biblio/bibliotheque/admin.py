from django.contrib import admin
from .models import Etudiant, Livre, Emprunt, Notification
from django.contrib.auth.admin import UserAdmin

@admin.register(Etudiant)
class EtudiantAdmin(UserAdmin):
    model = Etudiant
    list_display = ('username', 'email', 'departement', 'filiere', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ("Informations supplémentaires", {"fields": ("departement", "filiere")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informations supplémentaires", {"fields": ("departement", "filiere")}),
    )

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'disponible')
    search_fields = ('titre', 'auteur')
    list_filter = ('disponible',)

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('livre', 'etudiant', 'date_emprunt', 'date_retour', 'rendu')
    list_filter = ('rendu',)
    search_fields = ('livre__titre', 'etudiant__username')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'message', 'date', 'lue')
    list_filter = ('lue',)
