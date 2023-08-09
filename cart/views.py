from django.shortcuts import render
from .forms import Product_CartGetForm
from .models import Product_Cart
def product_get_view(request):
    if request.method == 'POST':
        form = Product_CartGetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Product_CartGetForm()
    return render(request, 'cart/product_get.html', {'form': form})

def cart_list(request):
    cart= Product_Cart.objects.all()
    return render(request, 'cart/cart_list.html', {"cart": cart})


# def products_list(request):
#     products = Product.objects.all()
#     return render(request, 'inventory/products_list.html', {'products':products})


# def product_detail(request , id):
#     product = Product.objects.get(id=id)
#     return render(request , 'inventory/product_detail.html',{'product':product})




# def product_update_view(request, id):
#     product = Product.objects.get(id=id)

#     if request.method == 'POST':
#         form = ProductUploadForm(request.POST, instance=product)

#         if form.is_valid():
#             form.save()
#             return redirect("product_detail", id=product.id)
    
#     else:
#         form = ProductUploadForm(instance=product)

#     return render(request, "inventory/edit_product.html", {'form': form})

# def delete_product(request, id):
#     product= Product.objects.get(id=id)
#     product.delete()
#     return redirect("product_list_view")




