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
from.views import Expense,EstimateView,Estimate,InvoiceView,Invoice,InvoiceSetting,Taxes,Payments,ProvidentFund


urlpatterns = [
        path('expense-list', Expense.as_view(), name="expense_list"),
        path('estimate-view', EstimateView.as_view(), name="estimate_view"),
        path('estimate-list', Estimate.as_view(), name="estimate_list"),
        path('invoice-view', InvoiceView.as_view(), name="invoice_view"),
        path('invoice-list', Invoice.as_view(), name="invoice_list"),
        path('invoice_setting', InvoiceSetting.as_view(), name="invoice_setting"),
        path('taxes', Taxes.as_view(), name="taxes"),
        path('payment-list', Payments.as_view(), name="payment_list"),
        path('provident-fund', ProvidentFund.as_view(), name="provident_fund"),
]
