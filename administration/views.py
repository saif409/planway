from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from employee.models import Leader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class AssetsListView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        return render(request, "clients/clients-list.html")