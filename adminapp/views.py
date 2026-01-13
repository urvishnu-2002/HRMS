from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = EmployeeForm()
    return render(request, 'add.html', {'form': form})

def view(request):
    employees = Employee.objects.all()
    return render(request, 'view.html', {'employees': employees})