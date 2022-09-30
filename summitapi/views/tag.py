from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models.tag import Tag
from django.db.models import Q


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')
        depth = 2


class TagView(ViewSet):
    """summit tag view"""


    def retrieve(self, request, pk):
        """Handles GET requests for a single tag

        Returns:
            Response -- JSON serialized tag instance"""

        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handles GET requests to get all tags

        Returns: 
            Response -- JSON serialized list of tags"""
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

        
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized tag instance
            """
        label = Tag.objects.create(
            label=request.data["label"]
        )
        serializer = TagSerializer(label)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a tag

        Returns:
            Response -- Empty body with 204 status code
            """
        tag = Tag.objects.get(pk=pk)
        tag.label = request.data["label"]

        tag.save()

        return Response(None, status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE operations

        Returns
            Response -- HTTP_204_NO_CONTENT"""
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
