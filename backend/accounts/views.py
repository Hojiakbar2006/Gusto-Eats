from accounts.models import User
from config import settings
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import UserRegisterSerializer, LoginSerializer, LogoutUserSerializer, UserProfileSerializer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = get_user_model().objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user_data = serializer.data
        return Response({
            'data': user_data,
            'message': 'You have successfully registered',
            'status': status.HTTP_201_CREATED
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_otp(request):
    email = request.data.get('email')

    if not email:
        return Response({"detail": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(get_user_model(), email=email)
    otp_code = user.generate_otp()
    user.save()

    send_mail(
        "Password reset",
        f"Your OTP code for password reset is: {otp_code}\n\nKeep this code confidential and do not share it with anyone.",
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

    return Response({"message": "The OTP code has been sent to the email."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reset_password(request):
    email = request.data.get('email')
    otp_code = request.data.get('otp_code')
    new_password = request.data.get('new_password')
    new_password2 = request.data.get('new_password2')

    if not email:
        return Response({"detail": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

    if not otp_code:
        return Response({"detail": "OTP code not fount"}, status=status.HTTP_404_NOT_FOUND)
    
    if not new_password:
        return Response({"detail": "New password is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not new_password2:
        return Response({"detail": "New password is required"}, status=status.HTTP_400_BAD_REQUEST)

    if new_password != new_password2:
        return Response({"detail": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(get_user_model(), email=email)
    
    if not user.verify_otp(otp_code):
        return Response({"detail": "Invalid OTP code"}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()

    return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    serializer = LogoutUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"message":"successfully logged out"},status=status.HTTP_204_NO_CONTENT)
