from rest_framework import serializers
from base.models import Note
from django.contrib.auth.models import User


#Notes serializer
class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'content', 'created_at', 'updated_at']
