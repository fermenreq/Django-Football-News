from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth import authenticate
from django.contrib.auth.management.commands import changepassword
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def UserFormView(request):
    return render(request, "index.html", {})


def contact(request):
    titulo = "Contacta con nosotros"
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = "Formulario de contacto"
        
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "singutgon@gmail.com", "doblev@yahoo.es"]
        email_mensaje = "%s: %s enviado por %s" % (form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False       
            )
    context = {
        "form":form,
        "titulo": titulo,
    }
    
    return render(request, "forms.html", context)
