from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EtudiantViewset, LivreViewset, EmpruntViewset, NotificationViewset

# Créer un routeur pour les vues
router = DefaultRouter()
router.register(r'etudiants', EtudiantViewset, basename='etudiant')
router.register(r'livres', LivreViewset, basename='livre')
router.register(r'emprunts', EmpruntViewset, basename='emprunt')
router.register(r'notifications', NotificationViewset, basename='notification')
# Inclure les URLs du routeur dans les URLs de l'application

urlpatterns = [
    path('', include(router.urls)),
]


