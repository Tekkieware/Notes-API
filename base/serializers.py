from rest_framework import serializers
from base.models import Note
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


#Notes serializer
class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'content', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'name', 'isAdmin']
        
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
