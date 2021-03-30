from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
from clients.models import Clients, ClientsProject
from employee.models import Employee


class DashboardView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        client = Clients.objects.all().count()
        project = ClientsProject.objects.all().count()
        employee = Employee.objects.all().filter(is_active=True).count()
        context={
            'isact_dashboard': 'active',
            'client':client,
            'project':project,
            'employee':employee,

        }
        return render(request, 'dashboard/index.html', context)


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            user = request.POST.get('user', )
            password = request.POST.get('pass', )
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('dashboard')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password mismatch!')
    return render(request, "dashboard/login.html")



