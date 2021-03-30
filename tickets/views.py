from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from tickets.models import Tickets, PRIORITY_CHOICES
from django.contrib import messages
from clients.models import Clients
from clients.models import ClientsProject
from system.utils import filter_model, SoftDelete


# Create your views here.


class TicketList(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, filter):
        ticket_subjects = request.GET.get("ticket_subjects")
        status = request.GET.get("status")
        priority = request.GET.get("priority")
        from_date = request.GET.get("from")
        to_date = request.GET.get("to")
        lookups = ['ticket_subjects__icontains', 'status','priority','created_date__gte','created_date__lte']
        values =[ticket_subjects,status, priority,from_date,to_date]
        # multiple search
        ticket_obj = Tickets.objects.all().filter(is_delete=False)
        ticket_obj = filter_model(ticket_obj, lookups, values)

        count_ticket= Tickets.objects.all().filter(is_delete=False).count()
        new_ticket = Tickets.objects.all().filter(is_delete=False).filter(status=8).count()
        solved_ticket = Tickets.objects.all().filter(is_delete=False).filter(status=7).count()
        pending_ticket = Tickets.objects.all().filter(is_delete=False).filter(status=4).count()
        reopened_ticket = Tickets.objects.all().filter(is_delete=False).filter(status=2).count()
        on_Hold_ticket = Tickets.objects.all().filter(is_delete=False).filter(status=3).count()
        inprogress_ticket = Tickets.objects.all().filter(is_delete=False).filter(status=5).count()
        canceled_ticket = Tickets.objects.all().filter(is_delete=False).filter(status=6).count()
        new_ticket_cal = (new_ticket/count_ticket)*100
        solved_ticket_cal = (solved_ticket/count_ticket)*100
        pending_ticket_cal = (pending_ticket/count_ticket)*100
        reopened_ticket_cal = (reopened_ticket/count_ticket)*100
        on_Hold_ticket_cal =  (on_Hold_ticket/count_ticket)*100
        inprogress_ticket_cal = (inprogress_ticket/count_ticket)*100
        canceled_ticket_cal = (canceled_ticket/count_ticket)*100
        client_obj = Clients.objects.all()
        if filter == 'High':
            ticket_obj = Tickets.objects.all().filter(is_delete=False).filter(priority=1)[::-1]
        elif filter == 'Medium':
            ticket_obj = Tickets.objects.all().filter(is_delete=False).filter(priority=2)[::-1]
        elif filter == 'Low':
            ticket_obj = Tickets.objects.all().filter(is_delete=False).filter(priority=3)[::-1]

        context={
            "ticket":ticket_obj,
            "count_ticket":count_ticket,
            "new_ticket":new_ticket,
            "solved_ticket":solved_ticket,
            "pending_ticket":pending_ticket,
            "new_ticket_cal":new_ticket_cal,
            "solved_ticket_cal":solved_ticket_cal,
            "pending_ticket_cal":pending_ticket_cal,
            "client":client_obj,
            "reopened_ticket" : reopened_ticket,
            "on_Hold_ticket" : on_Hold_ticket,
            "inprogress_ticket" : inprogress_ticket,
            "canceled_ticket" : canceled_ticket,
            "reopened_ticket_cal":reopened_ticket_cal,
            "on_Hold_ticket_cal":on_Hold_ticket_cal,
            "inprogress_ticket_cal":inprogress_ticket_cal,
            "canceled_ticket_cal":canceled_ticket_cal,
            "priority":list(PRIORITY_CHOICES)

        }
        return render(request, "tickets/tickets_list.html", context)

    def post(self, request, filter):
        ticket_subjects = request.POST.get("ticket_subjects")
        priority = request.POST.get("priority")
        status = request.POST.get("status")
        clients_obj = request.POST.get("clients")
        client = Clients.objects.get(company_name=clients_obj)
        description = request.POST.get("description")
        file_upload = request.FILES.get("file_upload")
        tic_obj = Tickets(ticket_subjects=ticket_subjects,priority=priority,status=status,clients=client,description=description,file_upload=file_upload)
        tic_obj.save()
        messages.success(request, "Tickets Add Successfully")
        return redirect('ticket_list', filter='None')


def ticket_remove(request, id):
    obj = SoftDelete.delete(Tickets, id)
    messages.success(request, "Tickets Deleted Successfully")
    return redirect('ticket_list', filter='None')


class TicketUpdate(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        obj = Tickets.objects.get(id=id)
        obj.ticket_subjects = request.POST.get("ticket_subjects")
        obj.priority = request.POST.get("priority")
        obj.status = request.POST.get("status")
        clients_obj = request.POST.get("clients")
        obj.client = Clients.objects.get(company_name=clients_obj)
        obj.description = request.POST.get("description")
        if request.FILES.get("file_upload"):
            obj.file_upload = request.FILES.get("file_upload")
        obj.save()
        messages.success(request, "Tickets Update Successfully")
        return redirect('ticket_list', filter='None')


def change_status(request):
    if request.method == "GET":
        ticket_id = request.GET.get('tkid')
        status = request.GET.get('status')
        obj = Tickets.objects.get(id=ticket_id)
        obj.status = status
        obj.save()
        data = {}
        return JsonResponse(data)


def change_priority(request):
    if request.method == "GET":
        priority = request.GET.get('priority')
        ticket_id = request.GET.get('tkid')
        obj = Tickets.objects.get(id=ticket_id)
        obj.priority = priority
        obj.save()
        data = {}
        return JsonResponse(data)


class EmployeeExperience(View):

    def post(self, request):
        position = request.POST.get("position")
        organization_name = request.POST.get("organization_name")
        from_date = request.POST.get("from_date")
        date_to = request.POST.get("date_to")






