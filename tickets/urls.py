from django.urls import path
from.import views


urlpatterns = [
    path('list/<str:filter>/', views.TicketList.as_view(), name="ticket_list"),
    path('update/<int:id>/', views.TicketUpdate.as_view(), name="ticket_update"),
    path('change-status', views.change_status, name='change-status'),
    path('priority-status', views.change_priority, name='change-priority'),
    path('ticket-remove/<int:id>/', views.ticket_remove, name='ticket_remove'),

]
