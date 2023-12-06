from django.conf.urls.static import static
from django.urls import path
from student import settings
from . import views

urlpatterns = [
    path('', views.add_student),
    path('get_document/', views.get_document),
    path('view_student/', views.view_student),
    path('update_student/', views.update_student),
    path('delete_student/', views.delete_student),
    path('parents/', views.parents),
    path('date_to_data/', views.date_to_data),
]
