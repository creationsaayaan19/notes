from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):

   routes = [
      {
        'Endpoint':'/notes/',
        'method':'GET',
        'body':'None',
        'description':'Returns an Array of notes'
      },
      {
        'Endpoint':'/notes/id',
        'method':'GET',
        'body':'None',
        'description':'Returns a single note object'
      },
      {
        'Endpoint':'/notes/create/',
        'method':'POST',
        'body': {'body':""},
        'description':'Creates new note with data sent in post req'
      },
      {
        'Endpoint':'/notes/update/',
        'method':'PUT',
        'body':{'body':""},
        'description':'creates an existing note with data sent '
       },
       {
        'Endpoint':'/notes/id/delete/',
        'method':'DELETE',
        'body':None,
        'description':'Deletes and exiting note'
       },
    ] 
        
   return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)  # Remove this, as 'notes' is a queryset
    return Response(serializer.data)  # Return the serialized data

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)  # Remove this, as 'notes' is a queryset
    return Response(serializer.data)  # Return the serialized data

