from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models import ClimbType



class ClimbTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for activities
    """
    class Meta:
        model= ClimbType
        fields=('id', 'name', 'climb_type_image')
        depth = 2



class ClimbTypeView(ViewSet):
    """rare climbType view"""
    
    def retrieve(self, request, pk):
        """Handles GET requests for a single climb_type

        Returns:
            Response -- JSON serialized climb_type instance"""

        try:
            climb_type = ClimbType.objects.get(pk=pk)
            serializer = ClimbTypeSerializer(climb_type)
            return Response(serializer.data)
        except ClimbType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all climb_types
        
        Returns:
            Response -- JSON serialized list of climb_types
        """
        climb_types = ClimbType.objects.all()
        serializer = ClimbTypeSerializer(climb_types, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations
        
        Returns
            Response -- JSON serialized game instance
        """
        climb_type = ClimbType.objects.create(
            name = request.data["name"],
            climb_type_image = request.data["climb_type_image"]
        )
        
        serializer = ClimbTypeSerializer(climb_type)
        return Response(serializer.data)
    
    
    def update(self, request, pk):
        """Handle PUT requests for a climb type
        
        Returns: 
            Response -- Empty body with 204 status code
        """
        
        climb_type = ClimbType.objects.get(pk=pk)
        climb_type.name = request.data["name"]
        climb_type.climb_type_image = request.data["climb_type_image"]
        climb_type.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Handles DELETE requests for a climb_type
        
        Returns:
            Response -- Empty body with 204 status code"""
        climb_type = ClimbType.objects.get(pk=pk)
        climb_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)