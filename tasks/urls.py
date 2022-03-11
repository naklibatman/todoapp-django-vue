from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views
urlpatterns = [
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
