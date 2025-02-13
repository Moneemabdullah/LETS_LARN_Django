from first_app.form import contuctForm
from django.shortcuts import render

def index(request):
    return render(request, './first_app/home.html')


def about(request):
    if request.method == 'POST':
        name = request.POST.get('userName')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render (request, './first_app/about.html',{'name':name, 'email':email, 'select':select})     
        
    else: 
        return render (request, './first_app/about.html')


def submit_form(request):
    # print(request.POST)
    
        return render (request, './first_app/form.html')
    
    

def django_form(request):
    if request.method == 'POST':
        form = contuctForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destainetion:
            #     for chunck in file.chunks():
            #         destainetion.write(chunck)
            print(form.cleaned_data)  # This prints form data to the console
    else:
        form = contuctForm()


    return render(request, 'first_app/django_form.html', {'form': form})