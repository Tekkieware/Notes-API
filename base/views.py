from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Note
from base.serializers import NoteSerializer



#View to create new note or list all existing notes
@api_view(['GET', 'POST'])
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#View to fetch, update or delete an existing note
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    
    #check if note exists
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #return note detail
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    #update note
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delte note
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
