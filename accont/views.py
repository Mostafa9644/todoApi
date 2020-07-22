from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import RigisterationSerializer
from rest_framework.permissions import AllowAny

from rest_framework.authtoken.models import Token

@api_view(['POST',])
@permission_classes([AllowAny])
def rigistration_view(request):
    
    if request.method=='POST':
        serializer=RigisterationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account= serializer.save()
            data['response']='succesfully register a new user'
            data['email']=account.email
            data['username']=account.username
            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)