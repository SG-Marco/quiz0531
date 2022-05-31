from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_article, name='new_article'),
    path('category/', views.show_categories, name='show_categories')

]
