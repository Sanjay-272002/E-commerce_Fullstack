from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
# Create your views here
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CategorySerializer

    def post(self, request, format=None):
        queryset = Category.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        name = data['name']
        queryset = queryset.filter(name__iexact=name)
        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data)

   