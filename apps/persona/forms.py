from django import forms

from apps.persona.models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields = [
            'nombre',
            'apellido',
            'dni',
            'sexo',
            'fecha_nac',
            'correo_electronico',
            'categoria',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni':'DNI',
            'sexo':'Sexo',
            'fecha_nac':'Fecha de Nacimiento',
            'correo_electronico':'Correo Electronico',
            'categoria':'Categoria',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido':forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(choices=(
                                            ('Hombre','Hombre'),
                                            ('Mujer','Mujer'),
                                          )),
            'fecha_nac': forms.DateInput(),
            'correo_electronico': forms.EmailInput(),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }