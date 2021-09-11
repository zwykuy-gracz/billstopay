from django.urls import path
from . import views

app_name = "bills"

urlpatterns = [
    path('', views.bills_list, name='bills-list'),
    path('create/', views.bill_create, name='bill-create'),
    path('<int:pk>/', views.bill_detail, name='bill-detail'),
    path('<int:pk>/update/', views.bill_update, name='bill-update'),
    path('<int:pk>/delete/', views.bill_delete, name='bill-delete'),
]
