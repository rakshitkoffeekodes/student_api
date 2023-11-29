from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student),
    path('view_student/', views.view_student),
    path('update_student/', views.update_student),
    path('delete_student/<int:pk>/', views.delete_student),
    path('student_document/', views.student_document),
    # path('view_document/', views.view_document),
]
