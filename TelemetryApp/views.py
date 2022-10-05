from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import variable
from django.http import JsonResponse

# Create your views here.

def home(request):
    variables = variable.objects.get(pk=1)
    context = {
        'variables':variables.velocidad
    }

    return render(request, 'home.html', context)

def project(request):
    lista = range(6)
    context = {
        'lista':lista
    }
    return render(request, 'project.html',context)

def gallery(request):

    return render(request, 'gallery.html',{})

def telemetry(request):

    return render(request, 'telemetry.html',{})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('home')

def get_variablesa(_request):
    var=variable.objects.order_by('-id')[:1]
    
    return JsonResponse({"users":list(var.values())})

def exportar_csv(request):
    queryset=variable.objects.all()
    options=variable._meta
    fields=[field.name for field in options.fields]
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='atachment; filename="datos.csv"'
    writer=csv.writer(response)
    writer.writerow([options.get_field(field).verbose_name for field in fields])

    for obj in queryset:
        writer.writerow([getattr(obj,field)for field in fields])
    return response
