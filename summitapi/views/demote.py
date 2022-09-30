from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models import Demote
from summitapi.models import SummitUser


class DemoteView(ViewSet):
    """post view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single demotion

        Returns:
            Response -- JSON serialized demotion
        """
        try:
            demote = Demote.objects.get(pk=pk)
            serializer = DemoteSerializer(demote)
            return Response(serializer.data)
        except Demote.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all demotions

        Returns:
            Response -- JSON serialized list of demotions
        """
        demotes = Demote.objects.all()
        demoteUser = request.query_params.get('demoteUser', None)
        if demoteUser is not None:
            demotes = demotes.filter(demoteUser=demoteUser)
        serializer = DemoteSerializer(demotes, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized demotion instance
        """
        user = SummitUser.objects.get(user=request.auth.user)

        demote = Demote.objects.create(
            demotedUser=SummitUser.objects.get(pk=request.data["demotedUser"]),
            approveUser=user
        )

        serializer = DemoteSerializer(demote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a post

        Returns:
            Response -- Empty body with 204 status code
        """
        user = SummitUser.objects.get(user=request.auth.user)

        demote = Demote.objects.get(pk=pk)
        if user.id == demote.approveUser:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        demote.secondApproveUser = user
        demote.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class DemoteSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    
    class Meta:
        model = Demote
        fields = ('id', 'demotedUser', 'approveUser', 'secondApproveUser')
        depth = 2
