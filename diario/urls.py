from django.urls import path
from diario_app import views
from django.urls import include

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('create/', views.create_entry, name='create_entry'),
    path('diario_app/', include('diario_app.urls')),

]
