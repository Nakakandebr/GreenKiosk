from django.shortcuts import render , redirect
from .forms import Product_CartGetForm
from .models import Product_Cart
def cart_upload_view(request):

    if request.method == 'POST':
        form = Product_CartGetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Product_CartGetForm()
    return render(request, 'cart/cart_get.html', {'form': form})

def cart_list(request):
    carts= Product_Cart.objects.all()
    return render(request, 'cart/cart_list.html', {"carts": carts})



def cart_detail(request , id):
    cart= Product_Cart.objects.get(id=id)
    return render(request , 'cart/cart_detail.html',{'cart':cart})




def cart_update_view(request, id):
    cart = Product_Cart.objects.get(id=id)

    if request.method == 'POST':
        form = Product_CartGetForm(request.POST, instance=cart)

        if form.is_valid():
            form.save()
            return redirect("cart_detail", id=cart.id)
    
    else:
        form = Product_CartGetForm(instance= cart)

    return render(request, "cart/edit_cart.html", {'form': form})

def delete_cart(request, id):
    cart= Product_Cart.objects.get(id=id)
    cart.delete()
    return redirect("cart_list_view")




