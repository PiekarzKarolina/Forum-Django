from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.TabView.as_view(), name='index'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/create_comment', views.create_comment, name='create_comment'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='categories'),
]