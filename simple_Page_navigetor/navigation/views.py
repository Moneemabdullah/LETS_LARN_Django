from django.shortcuts import render

def about(request):
    return render(request, 'navigation/about.html')
def contuct(requets):
        return render (requets,'navigation/contuct.html')
