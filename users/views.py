from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer, UserAuthSerializer, ConfirmationCodeSerializer
from .models import ConfirmationCode
import random

class AuthAPIView(APIView):
    serializer_class = UserAuthSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if user and user.is_active:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        
        return Response(
            {'error': 'Неверные данные или нету такого аккаунта'},
            status=status.HTTP_401_UNAUTHORIZED
        )

class RegistrationAPIView(APIView):
    serializer_class = UserRegisterSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            is_active=False
        )
        
        code = ''.join(random.choices('0123456789', k=6))
        ConfirmationCode.objects.create(user=user, code=code)

        return Response(
            {'user_id': user.id, 'code': code},
            status=status.HTTP_201_CREATED
        )

class ConfirmUserAPIView(APIView):
    serializer_class = ConfirmationCodeSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            code = ConfirmationCode.objects.get(code=serializer.validated_data['code'])
            user = code.user
            user.is_active = True
            user.save()
            code.delete()

            return Response(
                {'message': 'Аккаунт потвержден'},
                status=status.HTTP_200_OK
            )
            
        except ConfirmationCode.DoesNotExist:
            return Response(
                {'error': 'Неверный код'},
                status=status.HTTP_400_BAD_REQUEST
            )























# class AuthAPIView(APIView):
#     def post(self, request):
#         serializer = UserAuthSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(**serializer.validated_data)
#         if user and user.is_active:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response(data={'key': token.key})
#         return Response(status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserRegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#     user = User.objects.create_user(username=username, password=password, is_active=False)
#     confirmation_code = ConfirmationCode.objects.create(user=user)

#     return Response(status=status.HTTP_201_CREATED,
#                     data={'user_id': user.id, 'code': confirmation_code.code})

# @api_view(['POST'])
# def confirm_user(request):
#     serializer = ConfirmationCodeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     code = serializer.validated_data['code']
#     confirmation_code = ConfirmationCode.objects.get(code=code)
#     user = confirmation_code.user
#     user.is_active = True
#     user.save()
#     confirmation_code.delete()

#     return Response(status=status.HTTP_200_OK,
#                     data={'message': 'пользователь потвержден'})
