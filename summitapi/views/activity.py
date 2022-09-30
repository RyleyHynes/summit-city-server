from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    """JSON serializer for activities
    """
    class Meta:
        model=Activity
        fields=('id', 'type', 'activity_image_url')



class ActivityView(ViewSet):
    """rare activity view"""
    
    def retrieve(self, request, pk):
        """Handles GET requests for a single activity

        Returns:
            Response -- JSON serialized activity instance"""

        try:
            activity = Activity.objects.get(pk=pk)
            serializer = ActivitySerializer(activity)
            return Response(serializer.data)
        except Activity.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET requests to get all activities
        
        Returns:
            Response -- JSON serialized list of activities
        """
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        
        Returns
            Response -- JSON serialized game instance
        """
        activity = Activity.objects.create(
            type = request.data["type"],
            activity_image_url = request.data["activity_image_url"]
        )
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a activity
        
        Returns: 
            Response -- Empty body with 204 status code
        """
        
        activity = Activity.objects.get(pk=pk)
        activity.type = request.data["type"]
        activity.activity_image_url = request.data["activity_image_url"]
        activity.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Handles DELETE requests for a activity
        
        Returns:
            Response -- Empty body with 204 status code"""
        activity = Activity.objects.get(pk=pk)
        activity.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)