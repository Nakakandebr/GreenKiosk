from .forms import CustomerForm
from  django.shortcuts import render  , redirect
from .models import Customer


# Create your views here.
def customer_upload_view(request):
    if request.method =="POST" :
        form= CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm()
        
    return render(request, 'customer/customer_upload.html', {'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers':customers})


def customer_detail(request , id):
    customer  = Customer.objects.get(id=id)
    return render(request , 'customer/customer_detail.html',{'customer':customer})




def customer_update_view(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("customer_detail", id=customer.id)
    
    else:
        form = CustomerForm(instance=customer)

    return render(request, "customer/edit_customer.html", {'form': form})

def delete_customer(request, id):
    customer= Customer.objects.get(id=id)
    customer.delete()
    return redirect("customer_list_view")
