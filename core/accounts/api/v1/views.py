from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer, CustomAuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

class RegistrationApiView(generics.GenericAPIView):
    """
    registration user 
    """
    # permission_classes = [IsAuthenticated]
    serializer_class = RegistrationSerializer
    # queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                'email':serializer.validated_data['email']
            }
            return Response(data, status=201)
        return Response(serializer.errors,  status=400)

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class CustomDiscardAuthToekn(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)