from django.urls import path
from . import views

urlpatterns = [
    #assigning a view called post_list to the root URL. This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address. The last part, name='post_list', is the name of the URL that will be used to identify the view.
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
