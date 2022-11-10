from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models.hike_skill_level import HikeSkillLevel
from django.db.models import Q


class HikeSkillLevelSerializer(serializers.ModelSerializer):
    """JSON serializer for hike skill levels"""
    class Meta:
        model = HikeSkillLevel
        fields = ('id', 'level')
        depth = 2


class HikeSkillLevelView(ViewSet):
    """summit hike skill level view"""


    def retrieve(self, request, pk):
        """Handles GET requests for a single hike_skill_level

        Returns:
            Response -- JSON serialized hike skill level instance"""

        try:
            hike_skill_level = HikeSkillLevel.objects.get(pk=pk)
            serializer = HikeSkillLevelSerializer(hike_skill_level)
            return Response(serializer.data)
        except HikeSkillLevel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

            
    def list(self, request):
        """Handles GET requests to get all hike skill levels

        Returns: 
            Response -- JSON serialized list of hike skill levels"""
        search = self.request.query_params.get('search', None)
        hike_skill_levels = HikeSkillLevel.objects.all()

        if search is not None:
            hike_skill_levels = hike_skill_levels.filter(
                Q(level__contains=search)
            )

        serializer = HikeSkillLevelSerializer(hike_skill_levels, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized hike skill level instance
            """
        hike_skill_level = HikeSkillLevel.objects.create(
            level=request.data["level"]
        )
        serializer = HikeSkillLevelSerializer(hike_skill_level)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a tag
        
        Returns:
            Response -- Empty body with 204 status code
            """
        hike_skill_level = HikeSkillLevel.objects.get(pk=pk)
        hike_skill_level.level=request.data["level"]

        hike_skill_level.save()
        
        return Response(None, status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE operations
        
        Returns
            Response -- HTTP_204_NO_CONTENT"""
        hike_skill_level = HikeSkillLevel.objects.get(pk=pk)
        hike_skill_level.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
