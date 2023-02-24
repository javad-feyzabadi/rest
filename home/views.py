from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from . models import Person
from . serializers import PersonSerializer

class Home(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person,many = True)
        return Response(data=ser_data.data,status= status.HTTP_200_OK)



 