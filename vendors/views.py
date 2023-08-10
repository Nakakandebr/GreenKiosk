
from django.shortcuts import render, redirect
from .forms import VendorUploadForm
from .models import Vendor

def vendor_upload_view(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendors_list')  # Redirect to the list of vendors after successful upload
    else:
        form = VendorUploadForm()

    return render(request, 'vendor/vendor_upload.html', {'form': form})

def vendors_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendors_list.html', {'vendors': vendors})

def vendor_detail(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})  # Changed 'product' to 'vendor'

def vendor_update_view(request, id):
    vendor = Vendor.objects.get(id=id)

    if request.method == 'POST':
        form = VendorUploadForm(request.POST, instance=vendor)  # Pass the instance to the form

        if form.is_valid():
            form.save()
            return redirect("vendor_detail", id=vendor.id)
    else:
        form = VendorUploadForm(instance=vendor)

    return render(request, "vendor/edit_vendor.html", {'form': form})

def delete_vendor(request, id):
    vendor = Vendor.objects.get(id=id)  # Changed 'product' to 'vendor'
    vendor.delete()
    return redirect("vendors_list")  # Redirect to the list of vendors after deleting

