from django import forms

class contuctForm(forms.Form):
    name = forms.CharField(label='User name')
    
    file = forms.FileField()
    
    
    email = forms.EmailField(label='User Email')
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    chack = forms.BooleanField()
    birth = forms.DateField()
    appoinment = forms.DateTimeField()
    
    C = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(label='Size', choices=C)
    
    MEAL = [('P', 'Paperony'), ('M', 'Msroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL)
    


