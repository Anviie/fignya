from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:id>', post_detail, name='post_detail'),
    path('<int:post_id>/comment', post_comment, name='post_comment'),
    # path('', post_list, name='post_list'),
    
    # not used - path('<int:id>/', post_detail, name='post_detail'),

]