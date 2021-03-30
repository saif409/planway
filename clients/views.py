from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Clients,ClientsProject
from employee.models import Leader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class ClientListView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        client_obj = Clients.objects.all().filter(is_active=True)
        context = {
            'client':client_obj
        }
        return render(request, "clients/clients-list.html", context)


class InactiveClientListView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        client_obj = Clients.objects.all().filter(is_active=False)

        context = {
            'client':client_obj
        }
        return render(request, "clients/inactive_clients-list.html", context)


def create_client(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        name = request.POST.get("name")
        profile_picture = request.POST.get("profile_picture")
        designation = request.POST.get("designation")
        clients_id = request.POST.get("clients_id")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        nid = request.POST.get("nid")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        comapny = Clients.objects.filter(company_name=company_name)
        if comapny.exists():
            messages.warning(request, "Company Name Already Exists")
            return redirect('clients')
        else:
            clients_obj = Clients(company_name=company_name, name=name, profile_picture=profile_picture, designation=designation, clients_id=clients_id, phone=phone,email=email,
                                  nid =nid,address=address, gender=gender)
            clients_obj.save()
            messages.success(request, "Clients Profile Created Successfully !!")
            return redirect('clients')


class ClientsView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        client_obj = get_object_or_404(Clients, id=id)
        client_project = ClientsProject.objects.all().filter(company_name=client_obj)
        context={
            'client':client_obj,
            'client_project':client_project
        }
        return render(request, "clients/client-profile.html", context)


def client_remove(request, id):
    obj = get_object_or_404(Clients, id=id)
    obj.is_active = False
    obj.save()
    messages.success(request, "Clients Remove Successfully")
    return redirect('clients')