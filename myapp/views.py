from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST': # Если пользователь отправил форму - обрабатываем данные
        form = ContactForm(request.POST) # передаем отправленные данные в форму
        if form.is_valid(): # джанго проверяет форму
            return redirect('success')

    else:
        form = ContactForm()

    return render(request, 'contact.html' , {'form' : form})

def success(request):
    return render(request, 'success.html')