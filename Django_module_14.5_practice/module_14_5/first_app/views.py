from django.shortcuts import render
from first_app.forms import ExampleForm
# Create your views here.
def home(request):
    form = ExampleForm()
    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['files']
            with open('./first_app/upload/' + files.name, 'wb+') as destination:
                for chunk in files.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    return render(request, './first_app/home.html', {'form': form})