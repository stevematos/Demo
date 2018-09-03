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
            'dni': forms.NumberInput(attrs={
                                            'class': 'form-control',
                                            'id': 'number_field',
                                            'oninput': 'limit_input(8)'
                                    }),
            'sexo': forms.Select(choices=(
                                            ('Hombre','Hombre'),
                                            ('Mujer','Mujer'),
                                          ),
                                attrs={
                                    'class': 'form-control',
                                } ),
            'fecha_nac': forms.DateInput(attrs={
                                    'class': 'form-control',
                                    'placeholder':'Ejemplo: XX/XX/XXXX',
                                } ),
            'correo_electronico': forms.EmailInput(attrs={
                                    'class': 'form-control',
                                } ),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if not len(dni)==8:
            raise forms.ValidationError('El dni debe contener 8 digitos')
        return dni