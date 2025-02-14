from django.shortcuts import render
from model_form.forms import MyModelFrom
# Create your views here.
def model_form(request):
    form = MyModelFrom()
    if request.method == 'POST':
        form = MyModelFrom(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    return render(request,'./model_form/model_form.html', {'form': form})