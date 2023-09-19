from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='todo_update'),
	path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='todo_delete'),
	path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_details'),
]