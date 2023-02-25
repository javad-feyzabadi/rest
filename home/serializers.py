from rest_framework import serializers

from . models import Question,Answer
from .custom_relation_field import UserEmailNameRelationField

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()



class QoestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()    
    # user = serializers.SlugRelatedField(read_only = True,slug_field='email')
    user = UserEmailNameRelationField(read_only = True)

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self,obj):
        result = obj.asnswers.all()
        return AnswerSerializer(instance=result,many = True).data


class AnswerSerializer(serializers.ModelSerializer):
    user = UserEmailNameRelationField(read_only = True)

    class Meta:
        model = Answer
        fields = '__all__' 
           