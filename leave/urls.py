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
    path('list/<str:filter>/', views.LeaveListView.as_view(), name='leave_list'),
    path('remove-leave/<int:id>/', views.remove_leave, name='remove_leave'),
    path('emplyee/leave/list/<int:id>', views.SingleEmployeeLeaveList.as_view(), name='employee_leave_list'),
    path('change_leave_status/', views.change_leave_status, name='change_leave_status'),
    path('add-leave/', views.LeaveAddView.as_view(), name='add_leave'),
    path('add-total-leave/', views.TotalLeaveAddView.as_view(), name='add_total_leave'),



]
