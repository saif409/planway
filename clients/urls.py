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
    path('list/', views.ClientListView.as_view(), name='clients'),
    path('inactive-client/', views.InactiveClientListView.as_view(), name='inactive_clients'),
    path('create_client/', views.create_client, name='create_client'),
    path('client_remove/<int:id>/', views.client_remove, name='client_remove'),
    path('details/<int:id>/', views.ClientsView.as_view(), name='client_details'),

]
