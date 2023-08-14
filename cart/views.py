from django.shortcuts import render, redirect
from .models import Product_Cart
from .forms import ProductCartGetForm



def cart_upload(request):
    if request.method == 'POST':
        form = ProductCartGetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_cart') 
           
    else:
        form = ProductCartGetForm()
    return render(request, 'cart/cart_upload.html', {'form': form})



def list_cart(request):
    cart_products = Product_Cart.objects.all()
    
    return render(request, 'cart/list_cart.html', {'cart_products': cart_products})



def cart_detail(request, id):
    cart = Product_Cart.objects.get(id=id)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def delete_cart(request, id):
    cart = Product_Cart.objects.get(id=id)
    cart.delete()
    return redirect('list_cart')

def cart_edit(request, id):
    cart = Product_Cart.objects.get(id=id)

    if request.method == 'POST':
        form = ProductCartGetForm(request.POST, instance= cart)

        if form.is_valid():
            form.save()
            return redirect("cart_detail", id= cart.id)
    
    else:
        form = ProductCartGetForm(instance= cart)

    return render(request, "cart/cart_edit.html", {'form': form})