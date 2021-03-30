from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View

from system.utils import filter_model, SoftDelete
from.models import Leave,TotalLeave
from employee.models import Employee, Department
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


class LeaveListView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, filter):
        employee_name = request.GET.get("employee_name")
        leave_type = request.GET.get("leave_type")
        status = request.GET.get("status")
        leave_from = request.GET.get("leave_from")
        leave_to = request.GET.get("leave_to")
        lookups = ['employee_name__icontains', 'status','leave_from__gte', 'leave_to__lte']
        values = [employee_name, leave_type, status, leave_from, leave_to]
        leave_obj = Leave.objects.all()
        obj = filter_model(leave_obj, lookups, values)
        user_obj = Employee.objects.all()
        pending_leave = Leave.objects.all().filter(is_delete=False).filter(status=2)
        if filter == "New":
            obj = Leave.objects.all().filter(is_delete=False).filter(status=1)[::-1]
        elif filter == "Pending":
            obj = Leave.objects.all().filter(is_delete=False).filter(status=2)[::-1]
        elif filter == "Approve":
            obj = Leave.objects.all().filter(is_delete=False).filter(status=3)[::-1]
        elif filter == "Rejected":
            obj = Leave.objects.all().filter(is_delete=False).filter(status=4)[::-1]

        context={
            "obj":obj,
            "pending_leave":pending_leave,
            'user_obj':user_obj
        }
        return render(request, "leave/leaves.html", context)


def change_leave_status(request):
    if request.method == "GET":
        leave_id = request.GET.get('leaveid')
        status = request.GET.get('status')
        obj = Leave.objects.get(id=leave_id)
        obj.status = status
        obj.save()
        data = {}
        return JsonResponse(data)



class LeaveAddView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        employee_name = request.POST.get('employee_name')
        employee_obj = Employee.objects.get(id=int(employee_name))
        leave_type = request.POST.get('leave_type')
        leave_from = request.POST.get('leave_from')
        leave_to = request.POST.get('leave_to')
        leave_Reason = request.POST.get('leave_Reason')
        add = Leave(employee_name=employee_obj, leave_type=leave_type,leave_from=leave_from, leave_to=leave_to, leave_Reason=leave_Reason)
        add.save()
        messages.success(request, "Leave Added Successfully")
        return redirect('leave_list', filter='Pending')


def remove_leave(request, id):
    obj = SoftDelete.delete(Leave, id)
    messages.success(request, "Leave Deleted Successfully")
    return redirect('leave_list', filter='Pending')


class TotalLeaveAddView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        obj = TotalLeave.objects.all().last()
        context={
            "obj":obj
        }
        return render(request, "leave/total_leave_add.html", context)

    def post(self,request):
        total = request.POST.get("total")
        obj = TotalLeave(total=total)
        obj.save()
        messages.success(request, "Total Leave Add Successfully !!")
        return redirect("add_total_leave")


class SingleEmployeeLeaveList(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        get_user = get_object_or_404(Employee, id=id)
        leave_obj = Leave.objects.all().filter(employee_name=get_user)
        context={
            "leave_obj":leave_obj
        }
        return render(request, "leave/single_employee_leave_list.html", context)


class AddDepartment(View):

    def post(self, request):
        department_name = request.POST.get("department_name")
        obj = Department(department_name=department_name)
        obj.save()
        messages.success(request, "Department Added Successfully")
        return redirect('')
