from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from base.models import Note
from base.serializers import NoteSerializer, UserSerializerWithToken, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



#View to create new note or list all existing notes
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def note_list(request):
    
    #fetch all existing notes
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    #save new note
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#View to fetch, update or delete an existing note
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def note_detail(request, pk):
    
    #check if note exists with id(pk)
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #read note detail
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    #update note
    elif request.method == 'PUT':
        if request.user == note.created_by:
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            message = {'detail': 'Authors reserve the exlusive rights to edit their notes'}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete note
    elif request.method == 'DELETE':
        if request.user == note.created_by:
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            message = {'detail': 'Authors reserve the exlusive rights to delete their notes'}
            return Response(message, status=status.HTTP_401_UNAUTHORIZED,)
        

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])
        )
        print('created')
        serializer = UserSerializerWithToken(user, many=False)

        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)