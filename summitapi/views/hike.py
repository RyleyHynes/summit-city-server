from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models.hike import Hike
from django.db.models import Q


class HikeSerializer(serializers.ModelSerializer):
    """JSON serializer for reactions"""
    class Meta:
        model = Hike
        fields = ('id','user', 'name', 'distance', 'location', 'estimated_length', 'description', 'attractions', 'completed', 'bucket_list', 'hike_image_url', 'activity', 'hike_skill_level', 'attraction_type')