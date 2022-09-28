from argparse import Action
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models import SummitUser, summit_user
from django.contrib.auth.models import User
from rest_framework.decorators import action
import uuid
from django.core.files.base import ContentFile
import base64



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'is_staff', 'is_active')
class ProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for profiles
    """
    user = UserSerializer()
    class Meta:
        model = SummitUser
        fields = ('id', 'user', 'address',
                  'phone_number', 'profile_image', 'bio')
        depth = 2



class ProfileView(ViewSet):
    """Summit Profiles list view"""

    def list(self, request):
        """Handle GET requests to get all profiles

        Returns:
            Response -- JSON serialized list of profiles
            """

        profiles = SummitUser.objects.all()

        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single profile

        Returns: 
            Response -- JSON serialized profile"""
        try:
            profile = SummitUser.objects.get(pk=pk)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)

        except SummitUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        """Handle PUT requests for a user
        
        Returns:
            Response -- Empty body with 204 status code
            """
        user = request.auth.user
        summit_user= SummitUser.objects.get(user=request.auth.user)
        if request.data.get("profile_image"):
            format, imgstr = request.data["profile_image"].split(';base64')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(
                imgstr), name=f'{uuid.uuid4()}.{ext}')
            summit_user.profile_image=data
            summit_user.save()
        user.username=request.data["username"]
        user.email=request.data["email"]
        user.first_name=request.data["first_name"]
        user.last_name=request.data["last_name"]

        user.save()
        return Response(None, status.HTTP_204_NO_CONTENT)



    @action(methods=['PUT'], detail=True)
    def user_active(self, request, pk):
        user = User.objects.get(pk=pk) 
        user.is_active = not user.is_active
        user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['PUT'], detail=True)
    def user_status(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_staff = request.data["is_staff"] 
        user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

