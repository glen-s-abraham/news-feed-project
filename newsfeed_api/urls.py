from django.urls import path,include
from rest_framework.routers import DefaultRouter

from newsfeed_api import views

router=DefaultRouter()
router.register('news_feed',views.NewsFeedViewSet)
router.register('news_feed/<str:cat>',views.NewsFeedViewSet)


urlpatterns=[
	path('',include(router.urls))
]