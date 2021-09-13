from django.urls import path
from . import views

app_name = "bills"

urlpatterns = [
    path('', views.BillListView.as_view(), name='bills-list'),
    path('create/', views.BillCreateView.as_view(), name='bill-create'),
    path('<int:pk>/', views.BillDetailView.as_view(), name='bill-detail'),
    path('<int:pk>/update/', views.bill_update, name='bill-update'),
    path('<int:pk>/delete/', views.bill_delete, name='bill-delete'),
]
