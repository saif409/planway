"""office_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from.views import PayrollItem,Employeesalary,SalaryView,SalarySetting

urlpatterns = [
        path('payroll-item', PayrollItem.as_view(), name="payroll_item"),
        path('employee-salary', Employeesalary.as_view(), name="employee_salary"),
        path('salary_view', SalaryView.as_view(), name="salary"),
        path('salary-setting', SalarySetting.as_view(), name="salary_setting")
]
