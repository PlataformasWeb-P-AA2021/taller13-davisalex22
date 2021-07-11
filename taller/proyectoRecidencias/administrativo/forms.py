from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento

# Form Edificio
class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del Edificio por favor'),
            'direccion': _('Ingrese la direccion por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo': _('Ingrese el tipo de Edificio por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese el nombre del Edificio por favor")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data['direccion']
        num_palabras = len(valor.split())

        if num_palabras < 1:
            raise forms.ValidationError("Ingrese la direccion por favor")
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        num_palabras = len(valor.split())
        
        if num_palabras < 1:
            raise forms.ValidationError("Ingrese la ciudad por favor")
        #  El nombre de la ciudad no puede iniciar con la letra mayúscula **L**
        if "L" in valor:
            raise forms.ValidationError("Ingrese ciudad valida")
        return valor

    def clean_tipo(self):       
        valor = self.cleaned_data['tipo']
        num_palabras = len(valor.split())
        
        if num_palabras < 1:
            raise forms.ValidationError("Ingrese el tipo de Edificio por favor")
        return valor
     
# Form Departamento   
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numCuartos', 'edificio']
    
    # Número de cuartos no puede ser 0, ni mayor a 7.
    def clean_numCuartos(self):
        valor = self.cleaned_data['numCuartos']
        if (valor) == 0 or (valor) > 7:
            raise forms.ValidationError("Ingrese un numero de cuartos valido")
        return valor
    
    # Costo de un departamento no puede ser mayor a $100 mil.
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if (valor) > 100000:
            raise forms.ValidationError("Ingrese un costo valido")
        return valor
    # El nombre completo de un propietario **no** debe tener menos de 3 palabras.
    def clean_propietario(self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese sus nombres y apellidos por favor")
        return valor
    
# Form DepartamentoEdificio
class DepartamentoEdificioForm(ModelForm):
    
    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numCuartos', 'edificio']
    # El nombre completo de un propietario **no** debe tener menos de 3 palabras.
    def clean_propietario(self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese sus nombres y apellidos por favor")
        return valor
    # Costo de un departamento no puede ser mayor a $100 mil.
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if (valor) > 100000:
            raise forms.ValidationError("Ingrese un costo valido")
        return valor
    # Número de cuartos no puede ser 0, ni mayor a 7.
    def clean_numCuartos(self):
        valor = self.cleaned_data['numCuartos']
        if (valor) == 0 or (valor) > 7:
            raise forms.ValidationError("Ingrese un numero de cuartos valido")
        return valor
    