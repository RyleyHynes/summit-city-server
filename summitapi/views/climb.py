from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models.climb import Climb
from summitapi.models.summit_user import SummitUser
from summitapi.models.climb_type import ClimbType
from summitapi.models.grade import Grade
from django.db.models import Q


class ClimbSerializer(serializers.ModelSerializer):
    """JSON serializer for climbs"""
    class Meta:
        model = Climb
        fields = ('id', 'name', 'description', 'description', 'location', 'climb_image_url', 'climb_type', 'grade' 'tags')


class ClimbView(ViewSet):
    """Climb View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Climb
        Returns:
            Response -- JSON serialized Climb"""
        try:
            climb = Climb.objects.get(pk=pk)
            serializer = ClimbSerializer(climb)
            return Response(serializer.data)
        except Climb.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all climbs

        Returns:
            Response -- JSON serialized list of hikes"""
        # artist_show = request.query_params.get('show', None)
        search = self.request.query_params.get('search', None)
        climbs = Climb.objects.all()
        # if artist_show is not None:
        #     climb = climb.filter(show_id=artist_show)

        if search is not None:
            climbs = climbs.filter(
                Q(name__contains=search) |
                Q(description__contains=search) |
                Q(location__contains=search)
            )

        tag = request.query_params.get('tag_id', None)
        user = self.request.query_params.get('user_id', None)

        if user is not None:
            climbs = climbs.filter(user_id=user)
        if tag is not None:
            climbs = climbs.filter(tags=tag)

        serializer = ClimbSerializer(climbs, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized climb instance
            """

        climb_type = ClimbType.objects.get(
            pk=request.data["climb_type"])
        grade = Grade.objects.get(pk=request.data["grade"])

        climb = Climb.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            location=request.data["location"],
            climb_image_url=request.data["climb_image_url"],
            climb_type=climb_type,
            grade=grade
        )
        climb.tags.set(request.data["tags"])

        serializer = ClimbSerializer(climb)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a climb

        Returns:
            Response -- Empty body with 204 status code
            """

        user = SummitUser.objects.get(user=request.auth.user)
        # because its coming back as an object
        climb_type = ClimbType.objects.get(
            pk=request.data["hike_type"])
        grade = Grade.objects.get(pk=request.data["grade"])

        climb = Climb.objects.get(pk=pk)
        if user.id != climb.user.id and user.user.is_staff == False:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        climb.name = request.data["name"]
        climb.description = request.data["description"]
        climb.location = request.data["location"]
        climb.climb_image_url = request.data["climb_image_url"]
        climb.climb_type = climb_type
        climb.grade = grade
        climb.tags.set(request.data["tags"])

        climb.save()

        return Response(None, status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE operations"""
        climb = Climb.objects.get(pk=pk)
        climb.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
