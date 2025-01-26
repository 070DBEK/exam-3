from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
]
