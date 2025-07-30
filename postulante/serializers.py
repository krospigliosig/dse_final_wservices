# postulante/serializers.py
from rest_framework import serializers
from .models import PostulanteModel

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostulanteModel
        fields = '__all__'
