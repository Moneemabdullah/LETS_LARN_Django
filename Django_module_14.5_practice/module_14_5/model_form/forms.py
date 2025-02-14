from django import forms 
from model_form.models import MyModel 
class MyModelFrom(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'