from django.db import models

class NewsItem(models.Model):
	"""Model to hold the news article"""
	CATEGORIES=[
		('BR','Breaking'),
		('IN','International'),
		('NT','National'),
		('ST','State'),
		('DT','District'),
		('LC','Local'),
		('CL','Classifieds'),
		('TC','Technology'),
		('SP','Sports')
	]

	title=models.CharField(max_length=255)
	author=models.CharField(max_length=50)
	written_on=models.DateTimeField(auto_now_add=True)
	place=models.CharField(max_length=50)
	feature_image=models.FileField(upload_to ='uploads/',default='None')
	category=models.CharField(choices=CATEGORIES,default='BR',max_length=10)
	article=models.CharField(max_length=500)

	def __str__(self):
		
		return self.title
