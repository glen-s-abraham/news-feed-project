from django.contrib import admin
from newsfeed_api import models
from django import forms

# Register your models here.


class NewsArticleForm(forms.ModelForm):
	"""to over ride article charfield to text area"""
	article = forms.CharField(widget=forms.Textarea)

	class Meta:
		model=models.NewsItem
		fields=('title','author','place','feature_image','category','article')


class NewsModelAdmin(admin.ModelAdmin):
	"""Over ride default form"""
	form=NewsArticleForm

admin.site.register(models.NewsItem,NewsModelAdmin)