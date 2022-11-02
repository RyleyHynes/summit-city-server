from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models import SummitUser
from summitapi.models import my_hike
from summitapi.models.my_hike import MyHike
from summitapi.views.hike import HikeSerializer
from django.db.models import Q


class MyHikeSerializer(serializers.ModelSerializer):
    """JSON serializer for my_hike"""
    hikes = HikeSerializer(many=True)

    class Meta:
        model = MyHike
        fields = ('id', 'summit_user', 'hikes')
        depth = 2


class MyHikeView(ViewSet):
    """MyHike View"""

    def list(self, request):
        """Handle GET requests to get all my hikes"""

        summit_user = SummitUser.objects.get(user=request.auth.user)
        search = self.request.query_params.get('search', None)

        hike_list = MyHike.objects.filter(summit_user=summit_user)

        serializer = MyHikeSerializer(hike_list, many=True)
        if search is not None:
            hikes = hike_list[0].hikes.filter(
                Q(hike__name__icontains=search) |
                Q(hike__description__icontains=search) |
                Q(hike__location__icontains=search)
            )
            hike_serializer = HikeSerializer(hikes, many=True)
            serializer.data[0]['hikes'] = hike_serializer.data
        return Response(serializer.data)

    def create(self, request):
        """Handles Post for shows in my hike"""

        summit_user = SummitUser.objects.get(user=request.auth.user)

        my_hike,_ = MyHike.objects.get_or_create(
            summit_user=summit_user
        )
        my_hike.hikes.add(request.data["hike_id"])
        return Response({'message': 'hike added'}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """Handles DELETE for hike in my hike"""
        summit_user = SummitUser.objects.get(user=request.auth.user)
        my_hike_instance = MyHike.objects.get(summit_user=summit_user)
        my_hike_instance.hikes.remove(pk)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
