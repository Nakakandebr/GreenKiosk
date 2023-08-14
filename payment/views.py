from django.shortcuts import render , redirect
from .forms import PaymentUploadForm
from .models import Payment

def payment_create_view(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("payment_success")  # Redirect to a success page
    else:
        form = PaymentUploadForm()

    return render(request, 'payment_form.html', {'form': form})



# Create your views here.
# def payment_upload_view(request):
#     if request.method =="POST" :
#         form= PaymentUploadForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = PaymentUploadForm()
        
#     return render(request, 'payment/payment_upload.html', {'form': form})


# def payment_list(request):
#     payments = Payment.objects.all()
#     return render(request, 'payment/payment_list.html', {'payments':payments})

# def payment_detail(request , id):
#     payment = Payment.objects.get(id=id)
#     return render(request , 'payment/payment_detail.html',{'payment':payment})




# def payment_update_view(request, id):
#     payment = Payment.objects.get(id=id)

#     if request.method == 'POST':
#         form = PaymentUploadForm(request.POST, instance=payment)

#         if form.is_valid():
#             form.save()
#             return redirect("payment_detail", id=payment.id)
    
#     else:
#         form = PaymentUploadForm(instance=payment)

#     return render(request, "payment/edit_payment.html", {'form': form})

# def delete_payment(request, id):
#     payment= Payment.objects.get(id=id)
#     payment.delete()
#     return redirect("payment_list_view")
