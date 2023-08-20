from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from datetime import datetime, date
from .models import Signing, CustomUser
from .serializers import SigningSerializer

class SigningViewSet(viewsets.ModelViewSet):
    queryset = Signing.objects.all()
    serializer_class = SigningSerializer

@api_view(['POST'])
def clock_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    # Authenticate user
    user = authenticate(username=username, password=password)

    
    if user is not None:
        # do something
        today = date.today()
        existing_signing = Signing.objects.filter(user=user, date=today, clock_out_time__isnull=True).first()
        if existing_signing:
            return Response({"message": "Please clock out before clocking in again"}, status=status.HTTP_400_BAD_REQUEST)
        new_signing = Signing(user=user)
        new_signing.save()

        return Response({"message": "Clock-in successful"}, status=status.HTTP_201_CREATED)
        
    else:
        return Response({"message": "Invalid Credentials"})

@api_view(['POST'])
def clock_out(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        # do something
        today = date.today()
        existing_signing = Signing.objects.filter(user=user, date=today, clock_out_time__isnull=True).first()
        if existing_signing:
            existing_signing.clock_out_time = datetime.now()
            existing_signing.save()
            return Response({"message": "Clock-out successful"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Please clock in before clocking out again"}, status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response({"message": "Invalid Credentials"})
