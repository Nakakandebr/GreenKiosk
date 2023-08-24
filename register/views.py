# from django.shortcuts import render ,redirect
# from django.contrib.auth.models import User ,  auth
# from django.contrib import messages
# # Create your views here.
# def home(request):
#     return render(request , 'register/home.html')

# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')  

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username already exists')
#                 return redirect('register') 
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
#                 user.save()
#                 messages.success(request, 'User successfully registered')
#                 return redirect('login_user')  
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')
#     else:
#         return render(request, 'register/register.html')

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get['username']
#         password = request.POST.get['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request,user)
#             return redirect('home')
#         else:
#             messages.info(request,'Invalid username or password')
#             return redirect('login_user')
        
#     else:
#         return render(request, 'register/login.html')
    
# def logout_user(request):
#     auth.logout(request)
#     return redirect('home')
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def homePage(request):
    return render (request,'register/home.html')

def signupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'register/signup.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('product_upload_view')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'register/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')