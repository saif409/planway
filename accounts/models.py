from django.db import models
from clients.models import Clients, ClientsProject
from employee.models import Employee


TAX_STATUS = (
    (1, 'Active'),
    (2, 'Inactive')
)

PAYMENT_TYPE = (
    (1, 'Cash'),
    (2, 'Cheque')
)

INVOICE_STATUS = (
    (1, 'Pending'),
    (2, 'Paid'),
    (3, 'Partially Paid'),
)

EXPENSE_STATUS = (
    (1, 'Approved'),
    (2, 'Pending'),
)


class Tax(models.Model):
    tax_name = models.CharField(max_length=100)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(choices=TAX_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, related_name="invoices")
    project = models.ForeignKey(ClientsProject, on_delete=models.DO_NOTHING, related_name="invoices")
    tax = models.ForeignKey(Tax, on_delete=models.DO_NOTHING, related_name="invoices")
    client_address = models.CharField(max_length=256)
    billing_address = models.CharField(max_length=256)
    invoice_date = models.DateTimeField()
    due_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=100, decimal_places=2)
    discount = models.DecimalField(max_digits=100, decimal_places=2)
    grand_total = models.DecimalField(max_digits=1000, decimal_places=2)
    other_information = models.CharField(max_length=1000)
    status = models.IntegerField(choices=INVOICE_STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class InvoiceItems(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="invoice_items")
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    unit_cost = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=1000, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Payments(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")
    payment_date = models.DateTimeField()
    payment_amount = models.DecimalField(max_digits=1000, decimal_places=2)
    due_amount = models.DecimalField(max_digits=1000, decimal_places=2)
    payment_type = models.IntegerField(choices=PAYMENT_TYPE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Expense(models.Model):
    item_name = models.CharField(max_length=256)
    purchase_from = models.CharField(max_length=256)
    purchase_date = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name="expenses")
    amount = models.DecimalField(max_digits=1000, decimal_places=2)
    payment_type = models.IntegerField(choices=PAYMENT_TYPE, default=1)
    status = models.IntegerField(choices=EXPENSE_STATUS, default=2)
    attached_slip = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# class ProvidentFund(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name="provident_funds")
#     employee_share_amount = models.DecimalField(max_digits=1000, decimal_places=2)
#     employee_share_percentage = models.DecimalField(max_digits=5, decimal_places=2)
#     company_share_amount = models.DecimalField(max_digits=1000, decimal_places=2)
#     company_share_percentage = models.DecimalField(max_digits=5, decimal_places=2)
#     description = models.CharField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)