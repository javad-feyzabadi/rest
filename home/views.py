from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

from . models import Person,Question,Answer
from . serializers import PersonSerializer,QoestionSerializer,AnswerSerializer

from permissions import IsOwnerOrReadOnly



class Home(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person,many = True).data
        return Response(ser_data)


class QuestionListView(APIView):
    """
        List All Question
    """
    throttle_classes=[UserRateThrottle,AnonRateThrottle] 
    serializer_class = QoestionSerializer


    def get(self,request):
        questions =Question.objects.all()
        srz_data = QoestionSerializer(instance=questions,many = True)
        return Response(srz_data.data,status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
        Create A New Question
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QoestionSerializer

    def post(self,request):
        srz_data = QoestionSerializer(data=request.POST) 
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status= status.HTTP_201_CREATED)
        return Response(srz_data.errors,status= status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    """
        Update A Question
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QoestionSerializer


    def put(self,request,pk):
        question = Question.objects.get(pk = pk)
        self.check_object_permissions(request,question)
        srz_data = QoestionSerializer(instance=question,data=request.data,partial = True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    """
        Delete A Question
    """
    permission_classes = [IsOwnerOrReadOnly] 
    serializer_class = QoestionSerializer


    def delete(self,request,pk):
        question = Question.objects.get(pk = pk)
        question.delete()
        return Response({'message':'questions delete'},status=status.HTTP_200_OK)
 
