from rest_framework import serializers
from newsfeed_api import models


class NewsFeedSerializer(serializers.ModelSerializer):
	"""Serialiler to go with NewsItem model"""
	class Meta:
		model=models.NewsItem
		fields=('id','title','author','written_on','place','feature_image','category','article')