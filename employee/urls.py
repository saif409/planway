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


    path('list/<str:filter>/', views.UserListView.as_view(), name='employee'),
    path('employee_list/<str:filter>/', views.EmployeelistView.as_view(), name='employee_list'),
    path('profile/<int:id>/', views.ProfileView.as_view(), name='profile'),
    path('profile-update/<int:id>/', views.EmployeeUpdate.as_view(), name='profile_update'),
    path('register-profile/', views.register_employee, name='register_profile'),
    path('signout', views.signout, name='signout'),
    path('apply/', views.LeaveApplyView.as_view(), name='leave_apply'),
    path('leads', views.ProjectLeader.as_view(), name='Lead_list'),
    path('department-list/', views.DepartmentList.as_view(), name='department_list'),
    path('add-department/', views.AddDepartment.as_view(), name='add_department'),
    path('update-department/<int:id>/', views.UpdateDepartment.as_view(), name='update_department'),
    path('remove_department/<int:id>/', views.remove_department, name='remove_department'),
    path('designation-list/', views.DesignationList.as_view(), name='designation_list'),
    path('remove_designation/<int:id>/', views.remove_designation, name='remove_designation'),
    path('add-designation/', views.AddDesignation.as_view(), name='add_designation'),
    path('update-designation/<int:id>/', views.UpdateDesignation.as_view(), name='update_designation'),



    path('personal-information-update/<int:id>/', views.PersonalInformationUpdate.as_view(), name='personal_information_update'),
    path('employee-emergency-contact/<int:id>/', views.EmployeeEmergencyContact.as_view(), name='employee_emergency_contact'),
    path('employee-bank-information/<int:id>/', views.EmployeeBankInformation.as_view(), name='employee_bank_information'),



]
