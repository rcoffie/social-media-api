from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from social import views


urlpatterns = [
path('',views.PostList.as_view()),
path('post-detail/<int:pk>/', views.PostDetail.as_view()),
path('post-comment/',views.PostComment.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
