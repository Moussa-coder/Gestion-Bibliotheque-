from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Livre, Emprunt, Notification
from .serializers import LivreSerializer, EmpruntSerializer, NotificationSerializer, EtudiantSerializer
from django.contrib.auth import get_user_model

class EtudiantViewset(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAdminUser]  # Seuls les admin peuvent voir les étudiants

class LivreViewset(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [permissions.IsAuthenticated]

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

@api_view(['POST'])
def register_etudiant(request):
    """
    Inscription d'un nouvel étudiant.
    """
    User = get_user_model()
    serializer = EtudiantSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=request.data.get('password'),  #Mot de passe transmis brut
            departement=serializer.validated_data['departement'],
            filiere=serializer.validated_data['filiere'],
        )
        return Response({"message": "Étudiant inscrit avec succès"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_connected_user(request):
    
    serializer = EtudiantSerializer(request.user)
    return Response(serializer.data)
