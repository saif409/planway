"""office_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from.import views

urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name='project_list'),
    path('create-project/', views.CreateProject.as_view(), name='create_project'),
    path('update-project/<int:id>/', views.UpdateProject.as_view(), name='update_project'),
    path('remove-project/<int:id>/', views.remove_project, name='remove_project'),


]
