from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from letgo.models import Letgo
from letgo.serializers import LetgoSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def letgoAPI(request):
    if request.method == 'GET':
        letgos = Letgo.objects.all()
        serializer = LetgoSerializer(letgos, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data['key'])
        serializer = LetgoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view('GET','PUT','DELETE')
def letgodetailAPI(request,letgo_id):
    if request.method == "GET":
        letgo = Letgo.objects.get(id=letgo_id)
        letgo = get_object_or_404(Letgo, id=letgo_id)
        serializer = LetgoSerializer(letgo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        letgo = get_object_or_404(Letgo, id = letgo_id)
        serializer = LetgoSerializer(letgo,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        letgo = get_object_or_404(Letgo, id = letgo_id)
        letgo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
