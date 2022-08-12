from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from social import views


urlpatterns = [
path('',views.PostList.as_view()),
path('post-detail/<int:pk>/', views.PostDetail.as_view()),
path('post/<int:pk>/comment/',views.Comments.as_view()),
path('post/<int:pk>/create-comment/',views.CreateComment.as_view()),
path('update-delete-comment/<int:pk>/',views.UpdateComment.as_view()),

path('post-comment/<int:pk>/',views.postcomment.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
