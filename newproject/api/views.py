from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AppUser
from .serializer import UserSerializer

#GET API, To get the data of the user. Returns a Json with age, name and PK
#Returns all users
@api_view(['GET'])
def get_data(request):
    users = AppUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

#POST API, To get the data of the user. Takes a JSON with age and name then adds it to Db,sqlite3
@api_view(['POST'])
def create_data(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
#Checks if the user is present in the database.
def user_detail(request, pk):
    try:
        user = AppUser.objects.get(pk=pk)
    except AppUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GETs a particular User. Returns a Json with age, name and PK
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    #Update a particular User
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #Used to delete a User using PK
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
