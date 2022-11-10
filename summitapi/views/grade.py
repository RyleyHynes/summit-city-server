from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from summitapi.models import Grade
from django.db.models import Q



class GradeSerializer(serializers.ModelSerializer):
    """JSON serializer for ratings
    """
    class Meta:
        model = Grade
        fields = ('id', 'rating')


class GradeView(ViewSet):
    """rare grade view"""

    def retrieve(self, request, pk):
        """Handles GET requests for a single grade

        Returns:
            Response -- JSON serialized grade instance"""

        try:
            grade = Grade.objects.get(pk=pk)
            serializer = GradeSerializer(grade)
            return Response(serializer.data)
        except Grade.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all ratings

        Returns:
            Response -- JSON serialized list of ratings
        """
        search = self.request.query_params.get('search', None)
        grades = Grade.objects.all()

        if search is not None:
            grades = grades.filter(
                Q(rating__contains=search)
            )

        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        grade = Grade.objects.create(
            rating=request.data["rating"]
        )

        serializer = GradeSerializer(grade)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a grade

        Returns: 
            Response -- Empty body with 204 status code
        """

        grade = Grade.objects.get(pk=pk)
        grade.rating = request.data["rating"]
        grade.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for a grade

        Returns:
            Response -- Empty body with 204 status code"""
        grade = Grade.objects.get(pk=pk)
        grade.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
