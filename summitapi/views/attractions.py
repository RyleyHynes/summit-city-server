from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models.attraction import Attraction
from django.db.models import Q


class AttractionSerializer(serializers.ModelSerializer):
    """JSON serializer for attractions"""
    class Meta:
        model = Attraction
        fields = ('id', 'attraction_type')
        depth = 2


class AttractionView(ViewSet):
    """summit attraction view"""

    def list(self, request):
        """Handles GET requests to get all attractions

        Returns: 
            Response -- JSON serialized list of attractions"""
        attractions = Attraction.objects.all()
        serializer = AttractionSerializer(attractions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handles GET requests for a single attraction

        Returns:
            Response -- JSON serialized attraction instance"""

        try:
            attraction = Attraction.objects.get(pk=pk)
            serializer = AttractionSerializer(attraction)
            return Response(serializer.data)
        except Attraction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized attraction instance
            """
        attraction_type = Attraction.objects.create(
            attraction_type=request.data["attraction_type"]
        )
        serializer = AttractionSerializer(attraction_type)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handles DELETE operations

        Returns
            Response -- HTTP_204_NO_CONTENT"""
        attraction = Attraction.objects.get(pk=pk)
        attraction.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
