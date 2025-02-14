from django.shortcuts import render
from datetime import datetime
from random import randint
# Create your views here.
def details (request):
    d = {
        'name' : 'TAHSIN',
        'check_length' : ['a', 'b', 'c', 'd'],
        'int' : 7,
        'Today' : datetime.now(),

        'dictionary' : [
            {'name': 'joe', 'age': 31},
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
        ],
        'text': "My name is MD. Tahsin Ferdous \n I am a Student of Computer Science and Engineering \n I !hate coding \n Que mera bobo",

        'from' : datetime(randint(2020,2023), randint(1,11), randint(1,29)),
    }
    return render(request, 'first_app/details.html', context=d)