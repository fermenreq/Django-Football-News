from django import forms
from .models import *



#===============================================================================
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#      
#     class Meta:
#         model = Registrado
#         fields = ["email","password"]
#          
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         email_base, proveeder = email.split("@")
#         dominio,extension = proveeder.split('.')
#          
#         if not extension == "com":
#             raise forms.ValidationError("Porfavor, utiliza un email con la extension .COM")
#         else:
#             self.cleaned_data.get('email')
#         return email
#     
#     def clean_password(self):
#         password = self.cleaned_data.get("password")
#         return password
#===============================================================================
            
            
class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=90)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    