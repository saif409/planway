from django.shortcuts import render, get_object_or_404,redirect
from django.views import View

from system.utils import SoftDelete
from .models import Employee, EmergencyContact
from django.contrib.auth.models import User
from leave.models import Leave,TotalLeave
from.models import Department,Designation
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from employee.models import Leader

class UserListView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, filter):
        user_obj = None
        if filter == "None":
            user_obj = Employee.objects.all()[::-1]
        elif filter == "Active":
            user_obj = Employee.objects.all().filter(status=1)[::-1]
        elif filter == "InActive":
            user_obj = Employee.objects.all().filter(status=2)[::-1]
        elif filter == "Rejected":
            user_obj = Employee.objects.all().filter(status=3)[::-1]
        designation_obj = Designation.objects.all()
        department_obj = Department.objects.all()
        context={
            "user":user_obj,
            'isact_employeelist':'active',
            'designation':designation_obj,
            'department':department_obj
        }
        return render(request, 'employee/employees-list.html', context)


class EmployeelistView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, filter):
        user_obj = None
        if filter == "None":
            user_obj = Employee.objects.all()[::-1]
        elif filter == "Active":
            user_obj = Employee.objects.all().filter(status=1)[::-1]
        elif filter == "InActive":
            user_obj = Employee.objects.all().filter(status=2)[::-1]
        elif filter == "Rejected":
            user_obj = Employee.objects.all().filter(status=3)[::-1]

        context = {
            "user": user_obj,
            'isact_employeelist': 'active'
        }
        return render(request, 'employee/employees.html', context)


class ProfileView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        user_obj = get_object_or_404(Employee, id=id)
        context={
            "user":user_obj,
        }
        return render(request, 'employee/profile.html', context)


def register_employee(request):
    fname = request.POST.get('fname',)
    lname = request.POST.get('lname', )
    uname = request.POST.get('uname')
    password = request.POST.get('password', )
    email = request.POST.get("email")
    confirm_password = request.POST.get('confirm_password', )
    employee_id = request.POST.get("employee_id")
    joining_date = request.POST.get("joining_date")
    phone = request.POST.get("phone")
    designation = request.POST.get("designation")
    designation_obj = Designation.objects.get(designation_type=designation)
    department = request.POST.get("department")

    department_obj = Department.objects.get(department_name=department)
    profile_picture = request.FILES.get("profile_picture")
    user = User.objects.filter(username=uname)
    if user:
        messages.success(request, "Username Already Exist")
        return redirect('employee')
    else:
        auth_info = {
            'first_name': fname,
            'last_name': lname,
            'username': uname,
            'password': make_password(password),
        }
        user = User(**auth_info)
        user.save()
    user_obj = Employee(user=user, profile_picture=profile_picture, email=email, phone=phone, designation=designation_obj,
                        employee_id=employee_id, date_of_join=joining_date, department=department_obj)
    user_obj.save()
    messages.success(request, "Employee Create Successfully !!")
    return redirect('employee', filter=None)


class EmployeeUpdate(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        designation = Designation.objects.all()
        department = Department.objects.all()
        get_employee = Employee.objects.get(id=id)
        get_employee.user.first_name = request.POST.get('first_name')
        get_employee.user.last_name = request.POST.get('last_name')
        get_employee.user.username = request.POST.get('username')
        get_employee.user.password = request.POST.get('password')
        get_employee.email = request.POST.get("email")
        get_employee.confirm_password = request.POST.get('confirm_password', )
        get_employee.employee_id = request.POST.get("employee_id")
        get_employee.joining_date = request.POST.get("joining_date")
        get_employee.phone = request.POST.get("phone")
        designation_obj = request.POST.get("designation")
        get_employee.designation = Designation.objects.get(designation_type=designation_obj)
        department_obj = request.POST.get("department")
        get_employee.department = Department.objects.get(department_name=department_obj)
        if request.FILES.get("file_upload"):
            get_employee.profile_picture = request.FILES.get("profile_picture")
        get_employee.user.save()
        get_employee.save()
        messages.success(request, "Profile Update Successfully")
        return redirect('employee', filter=None)


class PersonalInformationUpdate(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request, id):
        user_obj = get_object_or_404(Employee, id=id)
        user_obj.passport_no = request.POST.get("passport_no")
        user_obj.nationality = request.POST.get("nationality")
        user_obj.religion = request.POST.get("religion")
        user_obj.martial_status = request.POST.get("martial_status")
        user_obj.no_of_chilldren = request.POST.get("no_of_chilldren")
        user_obj.employment_of_spouse = request.POST.get("employment_of_spouse")
        user_obj.save()
        messages.success(request, "Personal Information Successfully Update !!")
        return redirect('profile', id=id)


class EmployeeEmergencyContact(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        user_obj = get_object_or_404(Employee, id=id)
        name = request.POST.getlist("name[]")
        relationship = request.POST.getlist("relationship[]")
        phone = request.POST.getlist("phone[]")
        phone_another = request.POST.getlist("phone_another[]")
        for i in range(len(name)):
            emergency_contact_obj = EmergencyContact(name=name[i], relationship=relationship[i], phone=phone[i], phone_another=phone_another[i])
            emergency_contact_obj.save()
            user_obj.emergency_contact.add(emergency_contact_obj)
        messages.success(request, "Employee emergency contact added successfully !!")
        return redirect('profile', id=id)


class EmployeeBankInformation(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request, id):
        user_obj = get_object_or_404(Employee, id=id)
        user_obj.bank_name = request.POST.get("bank_name")
        user_obj.bank_account_no = request.POST.get("bank_account_no")
        user_obj.ifsc_code = request.POST.get("ifsc_code")
        user_obj.pan_no = request.POST.get("pan_no")
        user_obj.save()
        messages.success(request, "Bank Information Update Successfully !!")
        return redirect('profile', id=id)


def signout(request):
    logout(request)
    return redirect('login')


class LeaveApplyView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "leave/leave_apply.html")

    def post(self, request):
        user = request.user
        leave_time_from = request.POST.get('leave_time_from')
        leave_time_to = request.POST.get('leave_time_to')
        emergency_contact_no = request.POST.get('emergency_contact_no')
        reason_of_leave = request.POST.get('')
        leave_date = request.POST.get()
        leave_from = request.POST.get()
        leave_to = request.POST.get()
        leave_type = request.POST.get()
        leave_obj = Leave(user=user, reason_of_leave=reason_of_leave, leave_date=leave_date,leave_from=leave_from,leave_to=leave_to,leave_type=leave_type,emergency_contact_no=emergency_contact_no,
                          leave_time_to=leave_time_to,leave_time_from=leave_time_from)
        leave_obj.save()
        messages.success(request, "Your Leave Application Submit To Our HR, Please Wait For Leave Approval")
        return redirect('leave_apply')


class LeaveListView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, "leave/leave_list.html")


class TotalLeaveAddView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "leave/total_leave_add.html")


class ProjectLeader(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        leader_obj = Leader.objects.all()[::-1]
        context={
            "leader": leader_obj
        }
        return render(request, "project_leader/leads.html", context)


class DepartmentList(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        departments = Department.objects.all().filter(is_delete = False)[::-1]
        context={
            "departments":departments
        }
        return render(request, "department/departments.html", context)


class UpdateDepartment(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        dept_obj = get_object_or_404(Department, id=id)
        department_name = request.POST.get('department_name')
        department = Department.objects.filter(department_name=department_name)
        dept_obj.department_name = department_name
        dept_obj.save()
        messages.success(request, "Department name update successfully")
        return redirect('department_list')


class AddDepartment(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        department_name = request.POST.get("department_name")
        dept_obj = Department.objects.filter(department_name=department_name)
        if dept_obj.exists():
            messages.info(request, "Department name already exits !!")
            return redirect('department_list')
        else:
            obj = Department(department_name=department_name)
            obj.save()
            messages.success(request, "Department Added Successfully")
            return redirect('department_list')


def remove_department(request, id):
    obj = get_object_or_404(Department, id=id)
    desi_obj = Designation.objects.filter(department_name=obj.id)
    for i in desi_obj:
        i.is_delete = True
        i.save()
    obj_remove = SoftDelete.delete(Department, id)
    messages.success(request, 'Department Remove Successfully !!')
    return redirect('department_list')


class DesignationList(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        department = Department.objects.all()
        designation_obj = Designation.objects.all().filter(is_delete=False)[::-1]
        context={
            'designation':designation_obj,
            'department': department
        }
        return render(request, "designation/designations.html", context)


def remove_designation(request, id):
    obj = SoftDelete.delete(Designation, id)
    messages.success(request, "Designation removed successfully")
    return redirect('designation_list')


class AddDesignation(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        desination_obj = request.POST.get("designation")
        department_obj = request.POST.get('department')
        department = Department.objects.get(id=int(department_obj))
        designation = Designation.objects.filter(designation_type=desination_obj)
        if designation.exists():
            messages.warning(request, "Designation Already Exits !!")
            return redirect('designation_list')
        else:
            designation = Designation(designation_type=desination_obj,department_name=department)
            designation.save()
            messages.success(request, "Designation added successfully")
            return redirect('designation_list')


class UpdateDesignation(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        des_obj = get_object_or_404(Designation, id=id)
        des_obj.designation_type= request.POST.get("designation")
        department_obj = request.POST.get('department')
        des_obj.department = Department.objects.get(id=int(department_obj))
        des_obj.save()
        messages.success(request, "Designation added successfully")
        return redirect('designation_list')
