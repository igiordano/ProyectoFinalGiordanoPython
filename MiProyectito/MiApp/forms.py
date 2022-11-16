from django import forms

class CrearCursoForm(forms.Form):

    nombre = forms.CharField(min_length=5,max_length=40)
    comision = forms.IntegerField()

class CrearinstructorForm(forms.Form):
    nombre= forms.CharField(min_length=5,max_length=40)
    apellido= forms.CharField(min_length=5,max_length=40)
    email= forms.EmailField()
    profesion= forms.CharField(min_length=5,max_length=30)