from rest_framework import generics
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


'''Método POST APIView: Creación de Usuario'''
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


''' Login '''
class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    '''Post'''
    def post(self, request, *args, **kwargs):
        ## Aqui se guardan y validan los datos que el usuario ingresó en el login
        serializers = self.serializer_class(data=request.data, context={'request':request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']

        ## Creacion del token
        token,created = Token.objects.get_or_create(user=user)

        ## Al iniciar sesion, el Response devolverá el Token y los datos del usuario logueado
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.id,
            'email': user.email,
            'name': user.name
        })