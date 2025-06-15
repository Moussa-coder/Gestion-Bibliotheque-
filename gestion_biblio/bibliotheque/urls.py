from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EtudiantViewset, LivreViewset, EmpruntViewset, NotificationViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_etudiant
from .views import register_etudiant, get_connected_user

# Créer un routeur pour les vues
router = DefaultRouter()
router.register(r'etudiants', EtudiantViewset, basename='etudiant')
router.register(r'livres', LivreViewset, basename='livre')
router.register(r'emprunts', EmpruntViewset, basename='emprunt')
router.register(r'notifications', NotificationViewset, basename='notification')
# Inclure les URLs du routeur dans les URLs de l'application

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', register_etudiant, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', get_connected_user, name='get_connected_user'),
]


