from django import forms

class Contact(forms.Form):
    nombre_contacto = forms.CharField(max_length=20,label='Nombre y Apellido', required=True, 
                        widget= forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=9, label='Telefono', required=True,
                widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=30, label='E-mail', required=True,
            widget= forms.EmailInput(attrs={'class':'form-control'}))
    mensaje = forms.CharField(max_length=300, label='Mensaje', required=True, 
                widget=forms.Textarea(attrs={'class':'form-control', 'rows': 4}))

