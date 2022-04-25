from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

## Serializer: transforma los datos de una tabla a objeto JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'name')
        extra_kwargs = {'password':{'write_only':True, 'min_length':8}}
    
    def create(self, validate_data):
        return get_user_model().objects.create_user(**validate_data)
    

## Serializer para el TOKEN del Login de usuario
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type':'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError('Invalid User Credentials')
        attrs['user'] = user
        return attrs