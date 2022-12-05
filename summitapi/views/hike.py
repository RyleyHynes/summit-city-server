from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models.hike import Hike
from summitapi.models.summit_user import SummitUser
from django.db.models import Q

from summitapi.models.hike_skill_level import HikeSkillLevel


class HikeSerializer(serializers.ModelSerializer):
    """JSON serializer for hikes"""
    class Meta:
        model = Hike
        fields = ('id', 'name', 'distance', 'location', 'estimated_length', 'description', 'hike_image_url', 'hike_skill_level', 'tags')
        depth = 2


class HikeView(ViewSet):
    """Hike View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Hike
        Returns:
            Response -- JSON serialized Hike"""
        try:
            hike = Hike.objects.get(pk=pk)
            serializer = HikeSerializer(hike)
            return Response(serializer.data)
        except Hike.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all hikes

        Returns:
            Response -- JSON serialized list of hikes"""
        # artist_show = request.query_params.get('show', None)
        search = self.request.query_params.get('search', None)
        hikes = Hike.objects.all()
        # if artist_show is not None:
        #     hike = hike.filter(show_id=artist_show)

        if search is not None:
            hikes = hikes.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(location__icontains=search) |
                Q(hike_skill_level__level__icontains=search)
            )

        tag = request.query_params.get('tag_id', None)
        user = self.request.query_params.get('user_id', None)

        if user is not None:
            hikes = hikes.filter(user_id=user)
        if tag is not None:
            hikes = hikes.filter(tags=tag)

        serializer = HikeSerializer(hikes, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized hike instance
            """

        hike_skill_level = HikeSkillLevel.objects.get(pk=request.data["hike_skill_level"])
        
        hike = Hike.objects.create(
            name=request.data["name"],
            distance=request.data["distance"],
            location=request.data["location"],
            estimated_length=request.data["estimated_length"],
            description=request.data["description"],
            hike_image_url=request.data["hike_image_url"],
            hike_skill_level=hike_skill_level
        )
        hike.tags.set(request.data["tags"])

        serializer = HikeSerializer(hike)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a hike

        Returns:
            Response -- Empty body with 204 status code
            """

        # user = SummitUser.objects.get(user=request.auth.user)
        # because its coming back as an object
        hike_skill_level = HikeSkillLevel.objects.get(
            pk=request.data["hike_skill_level"])

        hike = Hike.objects.get(pk=pk)
        # if user.id != hike.user.id and user.user.is_staff is False:
        #     return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        hike.name = request.data["name"]
        hike.distance = request.data["distance"]
        hike.location = request.data["location"]
        hike.estimated_length = request.data["estimated_length"]
        hike.description = request.data["description"]
        hike.hike_image_url = request.data["hike_image_url"]
        hike.hike_skill_level = hike_skill_level
        hike.tags.set(request.data["tags"])

        hike.save()

        return Response(None, status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE operations"""
        hike = Hike.objects.get(pk=pk)
        hike.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
