from django.urls import path

from . import api

urlpatterns = [
     path('', api.post_list, name='post_list'),
     path('feed/', api.post_list_feed, name='post_list_feed'),
     path('<uuid:pk>/', api.post_detail, name='post_detail'),
     path('<uuid:pk>/like/', api.post_like, name='post_like'),
     path('<uuid:pk>/comment/', api.post_create_comment, name='post_create_comment'),
     path('<uuid:pk>/delete/', api.post_delete, name='post_delete'),
     path('<uuid:pk>/report/', api.post_report, name='post_report'),
     path('comment/<uuid:pk>/like/', api.comment_like, name='comment_like'),
     path('comment/<uuid:pk>/dislike/', api.comment_dislike, name='comment_dislike'),
     path('profile/<uuid:id>/', api.post_list_profile, name='post_list_profile'),
     path('create/', api.post_create, name='post_create'),
     path('trends/', api.get_trends, name='get_trends'),
]