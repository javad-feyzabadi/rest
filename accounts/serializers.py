from rest_framework import serializers


def clean_email(value):
    if 'admin' in value:
       raise serializers.ValidationError('you cant select admin')
    return value


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    email = serializers.EmailField(required = True,validators = [clean_email])
    password1 = serializers.CharField(required = True,write_only = True)
    password2 = serializers.CharField(required = True,write_only = True)


    def validate_username(self,value):
        if value == 'admin':
            raise serializers.ValidationError('you cant select admin')
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('password dose not match')
        return data