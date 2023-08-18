
from django.shortcuts import render, redirect
from .forms import VendorUploadForm
from .models import Vendor

def vendor_upload_view(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST  , request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('vendors_list')  
    else:
        form = VendorUploadForm()

    return render(request, 'vendors/vendor_upload.html', {'form': form})



def vendors_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors/vendors_list.html', {'vendors': vendors})

def vendor_detail(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, 'vendors/vendor_detail.html', {'vendor': vendor}) 
 
def vendor_update_view(request, id):
    vendor = Vendor.objects.get(id=id)

    if request.method == 'POST':
        form = VendorUploadForm(request.POST, instance=vendor)  

        if form.is_valid():
            form.save()
            return redirect("vendor_detail", id=vendor.id)
    else:
        form = VendorUploadForm(instance=vendor)

    return render(request, "vendors/edit_vendor.html", {'form': form})

def delete_vendor(request, id):
    vendor = Vendor.objects.get(id=id) 
    vendor.delete()
    return redirect("vendors_list")  

