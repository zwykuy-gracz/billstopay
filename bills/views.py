from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DeleteView, CreateView
from .models import Bills
from .forms import billsForm, BillsModelForm

class LandingPageView(TemplateView):
    template_name = 'home.html'

def home_page(request):
    return render(request, 'home.html')

class BillListView(ListView):
    template_name = 'bills/bills_list.html'
    queryset = Bills.objects.all()
    context_object_name = 'bills'

# context = {
#         'objects_view':bills, <- by default in ListView
#     }

def bills_list(request):
    bills= Bills.objects.all()
    context = {
        'bills':bills,
    }
    return render(request, 'bills/bills_list.html', context)


class BillDetailView(DeleteView):
    template_name = 'bills/bill_detail.html'
    queryset = Bills.objects.all()
    context_object_name = 'bill'

def bill_detail(request, pk):
    bill = Bills.objects.get(id=pk)
    context = {
        'bill':bill,
    }
    return render(request, 'bills/bill_detail.html', context)


class BillCreateView(CreateView):
    template_name = 'bills/bill_create.html'
    form_class = BillsModelForm
    
    def get_success_url(self) -> str:
        return reverse('bills:bill-create')

def bill_create(request):
    form = BillsModelForm()
    if request.method == 'POST':
        form = BillsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bills')
    context = {
        'form': form,
    }
    return render(request, 'bills/bill_create.html', context)


def bill_update(request, pk):
    bill = Bills.objects.get(id=pk)
    form = BillsModelForm(instance=bill)
    if request.method == 'POST':
        form = BillsModelForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('/bills')
    context = {
        'form': form,
        'bill':bill,
    }
    return render(request, 'bills/bill_update.html', context)

def bill_delete(request, pk):
    bill = Bills.objects.get(id=pk)
    bill.delete()
    return redirect('/bills')

# def bill_create(request):
#     form = billsForm()
#     if request.method == 'POST':
#         form = billsForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             name = form.cleaned_data['name']
#             amount = form.cleaned_data['amount']
#             dueDate = form.cleaned_data['dueDate']
#             automaticPayment = form.cleaned_data['automaticPayment']
#             payd = form.cleaned_data['payd']
#             #agent = Agent.objects.first()
#             Bills.objects.create(
#                 name = name,
#                 amount = amount,
#                 dueDate = dueDate,
#                 automaticPayment = automaticPayment,
#                 payd = payd,
#             )
#             return redirect('/bills')
#     context = {
#         'form': form,
#     }
#     return render(request, 'bills/bill_create.html', context)