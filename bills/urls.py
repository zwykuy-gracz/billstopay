from django.urls import path
from . import views

app_name = "bills"

urlpatterns = [
    path('', views.BillListView.as_view(), name='bills-list'),
    path('<int:pk>/', views.BillDetailView.as_view(), name='bill-detail'),
    path('<int:pk>/update/', views.BillUpdateView.as_view(), name='bill-update'),
    path('<int:pk>/delete/', views.BillDeleteView.as_view(), name='bill-delete'),
    path('create/', views.BillCreateView.as_view(), name='bill-create'),
]
