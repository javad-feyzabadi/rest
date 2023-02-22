from django.contrib.auth.models import User

from rest_framework import serializers



def clean_email(value):
    if 'admin' in value:
       raise serializers.ValidationError('you cant select admin')
    return value


class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(required = True,write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True},
            'email':(clean_email,),
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
             
    def validate_username(self,value):
        if value == 'admin':
            raise serializers.ValidationError('you cant select admin')
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('password dose not match')
        return data