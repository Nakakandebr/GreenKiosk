from django.shortcuts import render , redirect
from .forms import CategoriesUploadForm
from .models import Categories


# Create your views here.
def categories_upload_view(request):
    if request.method =="POST" :
        form= CategoriesUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriesUploadForm()
        
    return render(request, 'categories/categories_upload.html', {'form': form})


def categories_list(request):
    categories = Categories.objects.all()
    return render(request, 'categories/categories_list.html', {'categories':categories})


def category_detail(request , id):
    category = Categories.objects.get(id=id)
    return render(request , 'categories/categories_detail.html',{'category':category})




def category_update_view(request, id):
    category = Categories.objects.get(id=id)

    if request.method == 'POST':
        form = CategoriesUploadForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect("category_detail", id=category.id)
    
    else:
        form = CategoriesUploadForm(instance=category)

    return render(request, "category/edit_category.html", {'form': form})

def delete_category(request, id):
    product= Categories.objects.get(id=id)
    product.delete()
    return redirect("category_list_view")
