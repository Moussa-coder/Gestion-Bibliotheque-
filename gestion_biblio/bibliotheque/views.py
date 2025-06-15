from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Livre, Emprunt, Notification
from .serializers import LivreSerializer, EmpruntSerializer, NotificationSerializer
from django.contrib.auth import get_user_model

# Create your views here.
class EtudiantViewset(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = get_user_model()
    permission_classes = [permissions.IsAdminUser] #Seuls les admin peuvent voir les etudiants
    
class LivreViewset(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [permissions.IsAuthenticated]  # Tout utilisateur authentifié peut voir les livres

class EmpruntViewset(viewsets.ModelViewSet):
    serializer_class = EmpruntSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Emprunt.objects.all()
        return Emprunt.objects.filter(etudiant=user)

    def perform_create(self, serializer):
        serializer.save(etudiant=self.request.user)
        
class NotificationViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(etudiant=self.request.user)