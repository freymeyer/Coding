from django.shortcuts import render, HttpResponse
from .models import ToDoItem
from .forms import CalculatorForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def todos(request):
    items = ToDoItem.objects.all()
    return render(request, "todos.html", {"todos":items})

def counter(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0

    if request.method == 'POST':
        if 'increment' in request.POST:
            request.session['counter'] += 100
            print('Added counter')
        elif 'decrement' in request.POST:
            request.session['counter'] -= 100
            print('Taken counter')
        elif 'reset' in request.POST:
            request.session['counter'] = 0
            print('Reset counter')
        request.session.modified =True
    return render(request, "counter.html", {"counter": request.session['counter']})


def Password(request):
    if 'password' not in request.session:
        request.session['password'] = ''
    
    if request.method == 'POST':
        if 'alpha' in request.POST:
            request.session['password'] += 'alpha'
        elif 'beta' in request.POST:
            request.session['password'] += 'beta'
        elif 'cython' in request.POST:
            request.session['password'] += 'cython'
        elif 'reset' in request.POST:
            request.session['password'] = ''
        request.session.modified = True
        print(request.session['password'])
    return(render(request,"passwordmaker.html",{"password": request.session['password']}))        


def calculator(request):
    result = None

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            operator = form.cleaned_data['operator']
            num2 = form.cleaned_data['num2']

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
    else:
        form = CalculatorForm()

 

    
    return(render(request, 'calculator.html', {'form':form, 'result':result}))    