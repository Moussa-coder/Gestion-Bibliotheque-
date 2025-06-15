from rest_framework import serializers
from .models import Livre, Emprunt, Etudiant, Notification
from django.contrib.auth import get_user_model

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'departement', 'filiere']
        
class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = ['id', 'titre', 'auteur', 'image', 'disponible']
        
class EmpruntSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(read_only=True)  # Affiche les infos du livre
    livre_id = serializers.PrimaryKeyRelatedField(
        queryset=Livre.objects.all(), source='livre', write_only=True
    )
    etudiant = EtudiantSerializer(read_only=True)

    class Meta:
        model = Emprunt
        fields = ['id', 'livre', 'livre_id', 'etudiant', 'date_emprunt', 'date_retour', 'rendu']
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'etudiant', 'message', 'date', 'lue']