from django.db import models
from employee.models import Employee


class Salary(models.Model):
    # net_salary = basic_salary + dearness_allowance + house_rent_allowance + conveyance + medical_allowance
    #              + other_allowance - tax_deduction_at_source - provident_fund
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name="salary")
    net_salary = models.DecimalField(max_digits=50, decimal_places=2)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    dearness_allowance = models.DecimalField(max_digits=5, decimal_places=2)
    house_rent_allowance = models.DecimalField(max_digits=5, decimal_places=2)
    conveyance = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    other_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    tax_deduction_at_source = models.DecimalField(max_digits=10, decimal_places=2)
    provident_fund = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
