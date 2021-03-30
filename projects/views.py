from django.contrib.auth.models import User
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clients.models import ClientsProject, Clients
from system.utils import SoftDelete

# Create your views here.
from employee.models import Leader, Employee


class ProjectListView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        obj = ClientsProject.objects.all().filter(is_delete=False)[::1]
        leader_obj = Leader.objects.all()
        employee_obj = Employee.objects.all()
        client_obj = Clients.objects.all()
        context = {
            "obj": obj,
            'leader':leader_obj,
            "employee":employee_obj,
            "client":client_obj
        }
        return render(request, "project/projects.html", context)


class CreateProject(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        company_name = request.POST.get("company_name")
        company = Clients.objects.get(company_name=company_name)
        project_title = request.POST.get("project_title")
        start_date = request.POST.get("start_date")
        project_deadline = request.POST.get("project_deadline")
        project_leader = request.POST.get("project_leader")
        leader = Leader.objects.get(id=project_leader)
        project_employee = request.POST.getlist("project_employee[]")
        progress = request.POST.get("progress")
        project_description = request.POST.get("project_description")
        project_files = request.POST.get("project_files")
        priority = request.POST.get("priority")
        obj = ClientsProject(company_name=company,project_title=project_title,start_date=start_date,
                             project_deadline=project_deadline,project_leader=leader,
                             progress=progress,project_description=project_description,project_files=project_files,priority=priority)
        obj.save()
        for i in range(len(project_employee)):
            emp_obj = Employee.objects.get(id=project_employee[i])
            obj.project_employee.add(emp_obj)
        messages.success(request, "Project Create Successfully")
        return redirect('project_list')


class UpdateProject(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request, id):
        client_project = get_object_or_404(ClientsProject, id=id)
        company_name = request.POST.get("company_name")
        company = Clients.objects.get(company_name=company_name)
        project_title = request.POST.get("project_title")
        start_date = request.POST.get("start_date")
        project_deadline = request.POST.get("project_deadline")
        project_leader = request.POST.get("project_leader")
        leader = Leader.objects.get(id=project_leader)
        project_employee = request.POST.getlist("project_employee[]")
        progress = request.POST.get("progress")
        project_description = request.POST.get("project_description")
        project_files = request.POST.get("project_files")
        priority = request.POST.get("priority")

        client_project.company_name = company
        client_project.project_title = project_title
        client_project.start_date =start_date
        client_project.project_deadline=project_deadline
        client_project.project_leader = leader
        client_project.progress = progress
        client_project.project_description = project_description
        client_project.project_files =project_files
        client_project.priority =priority
        client_project.save()
        for i in range(len(project_employee)):
            emp_obj = Employee.objects.get(id=project_employee[i])
            client_project.project_employee.add(emp_obj)
        messages.success(request, "Update Project Successfully")
        return redirect('project_list')


def remove_project(request, id):
    obj = SoftDelete.delete(ClientsProject, id)
    messages.success(request, "Project Remove Successfully !!")
    return redirect('project_list')
