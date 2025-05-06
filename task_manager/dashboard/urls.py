from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # index, create, update, delete
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('in-progress/<int:id>/', views.in_progress, name='in_progress'),
    path('completed/<int:id>/', views.completed, name='completed'),
    path('update/<int:id>/', views.update, name='update'),
    path('undo-progress/<int:id>/', views.undo_progress, name='undo_progress'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('reset_all', views.reset_all, name='reset_all'),
    path('new_category/', views.new_category, name='new_category'),
    path('clear_categories5364/', views.clear_categories, name='clear_categories'),
]