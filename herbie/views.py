from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import testimonies,my_blog,SiteEditor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import contact
from django.views.generic import ListView,DetailView

# Create your views here.
def index(request):
    return render(request,'herbie/index.html',context={'editor':SiteEditor.objects.all()})


def about(request):
    return render(request,'herbie/about.html',context={'editor':SiteEditor.objects.all()})

def testimonials(request):
    return render(request,'herbie/testimonials.html',context={'testimonies':testimonies.objects.all()})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Successfully registered:{username}")
            login(request,user)
            messages.info(request,f"you are logged in as:{username}")
            return redirect('herbie:about')
        
        
      #fix this part,always shows error for two password fields dont match,delete next two lines and use form design like crispy
      #cant have two users with same name
      
        else:
            return render(request,'herbie/register.html',context = {'form':form})  
    else:
        form = UserCreationForm()
        return render(request,'herbie/register.html',context = {'form':form})


def logout_view(request):
    logout(request)
    messages.info(request,f'Succesfully logged out')
    return redirect('herbie:index')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password =  password)
            if user is not None:
                login(request,user)
                messages.success(request,f'Successfully logged in as :{username}')
                return redirect('herbie:dash')
            else:
                return render(request,'herbie/login.html',context={'form':form})
        else:
            return render(request,'herbie/login.html',context={'form':form})
                   
    else:
        form = AuthenticationForm()
        return render(request,'herbie/login.html',context={'form':form})
    
    
@login_required
def dash(request):
    return render(request,'herbie/dash.html')


def Contact(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        eml = request.POST.get('email')
        phn = request.POST.get('phone')
        msg = request.POST.get('message')
        c = contact(name = nm,email = eml,phone = phn,message = msg)
        c.save()
        return render(request,'herbie/index.html')
    else:
        return render(request,'herbie/contact.html')
    
    
    
def faq(request):
    return render(request,'herbie/faq.html')
        
def services(request):
    return render(request,'herbie/services.html')

class BlogPostView(ListView):
    model = my_blog
    template_name = 'herbie/blog.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = my_blog
    
    
        