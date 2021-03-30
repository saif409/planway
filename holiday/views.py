from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.contrib.auth.models import User
from leave.models import Leave,TotalLeave
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from.models import Holiday

# Create your views here.


class HolidayListView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        holiday_obj = Holiday.objects.all()[::-1]
        context={
            "holiday":holiday_obj
        }
        return render(request, "holiday/holidays.html", context)


def holiday_remove(request):
    obj = get_object_or_404(Holiday, id=id)
    obj.delete()
    return redirect('holiday_list')


def delete_selected(request):
    data = request.GET
    merchant_id = data.get('selected_id').split(',')
    print(merchant_id)
    if merchant_id[0] == '':
        messages.success(request, "Please Select Atleast One Row !!")
        return redirect('holiday_list')
    else:
        for id in merchant_id:
            obj = Holiday.objects.get(id=id)
            obj.delete()
        messages.success(request, "Holiday Deleted Successfully !!")
        return redirect('holiday_list')


def add_holiday(request):
    if request.method == "POST":
        title = request.POST.get("title")
        day = request.POST.get("day")
        holiday_date = request.POST.get("holiday_date")
        holi_obj = Holiday(title=title,holiday_date=holiday_date,day=day)
        holi_obj.save()
        messages.success(request, "Holiday Successfully Added !!")
        return redirect('holiday_list')
