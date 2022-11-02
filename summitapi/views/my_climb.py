from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models import SummitUser
from summitapi.models import my_climb
from summitapi.models.my_climb import MyClimb
from summitapi.views.climb import ClimbSerializer
from django.db.models import Q


class MyClimbSerializer(serializers.ModelSerializer):
    """JSON serializer for my_climb"""
    climbs = ClimbSerializer(many=True)

    class Meta:
        model = MyClimb
        fields = ('id', 'summit_user', 'climbs')
        depth = 2


class MyClimbView(ViewSet):
    """MyClimb View"""

    def list(self, request):
        """Handle GET requests to get all my climbs"""

        summit_user = SummitUser.objects.get(user=request.auth.user)
        search = self.request.query_params.get('search', None)

        climb_list = MyClimb.objects.filter(summit_user=summit_user)

        serializer = MyClimbSerializer(climb_list, many=True)
        if search is not None:
            climbs = climb_list[0].climbs.filter(
                Q(climb__name__icontains=search) |
                Q(climb__description__icontains=search) |
                Q(climb__location__icontains=search)
            )
            climb_serializer = ClimbSerializer(climbs, many=True)
            serializer.data[0]['climbs'] = climb_serializer.data
        return Response(serializer.data)

    def create(self, request):
        """Handles Post for shows in my climb"""

        summit_user = SummitUser.objects.get(user=request.auth.user)

        my_climb,_ = MyClimb.objects.get_or_create(
            summit_user=summit_user
        )
        my_climb.climbs.add(request.data["climb_id"])
        return Response({'message': 'climb added'}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """Handles DELETE for climb in my climb"""
        summit_user = SummitUser.objects.get(user=request.auth.user)
        my_climb_instance = MyClimb.objects.get(summit_user=summit_user)
        my_climb_instance.climbs.remove(pk)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
