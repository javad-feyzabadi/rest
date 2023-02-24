from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from . models import Person,Question,Answer
from . serializers import PersonSerializer,QoestionSerializer,AnswerSerializer

class Home(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person,many = True).data
        return Response(ser_data,status= status.HTTP_200_OK)


class QuestionView(APIView):

    def get(self,request):
        questions =Question.objects.all()
        srz_data = QoestionSerializer(instance=questions,many = True)
        return Response(srz_data.data,status=status.HTTP_200_OK)


    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass
 