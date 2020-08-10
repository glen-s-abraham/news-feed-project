from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from newsfeed_api import serializers
from newsfeed_api import models
from newsfeed_api import permissions
# Create your views here.

class NewsFeedViewSet(viewsets.ModelViewSet):
	"""API view for the users to access news items"""
	serializer_class=serializers.NewsFeedSerializer
	queryset=models.NewsItem.objects.all()
	permission_classes=(permissions.IsAdminUser,)
	filter_backends=[filters.OrderingFilter]
	ordering_fields=['written_on']
	ordering=['-written_on']

	def get_queryset(self):

		category = self.request.query_params.get('cat', None)
		
		
		if category:

			return models.NewsItem.objects.filter(category=category.upper())
		return models.NewsItem.objects.all()
        


def documentation(request):
	return render(request,'documentation.html')        
        