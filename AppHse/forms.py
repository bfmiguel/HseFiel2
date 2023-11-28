from django import forms

class permisotrabajoForms(forms.Form):
    nombre = forms.CharField()
    Operacion = forms.CharField()
    numero = forms.IntegerField()



class busquedaform(forms.Form):
    nombre = forms.CharField()
