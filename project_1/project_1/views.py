from django.http import HttpResponse


def homepage(request):
    return HttpResponse("this is homepage")
def contuct(request):
    return HttpResponse("this is contuct page")