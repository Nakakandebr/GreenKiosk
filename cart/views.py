from django.shortcuts import render
from .forms import Product_CartGetForm

# Create your views here.
def product_get_view(request):
    form = Product_CartGetForm()
    return render(request, 'cart/product_get.html', {'form': form})

