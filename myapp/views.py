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


from .forms import ContactForm, BookForm
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid(): 
            form.save() #ModelForm не просто проверяет данные — он может сохранить их в модель
            return redirect('book_success')
    else:
        form = BookForm()
    return render(request, 'book_form.html' , {'form' : form})

def book_success(request):
    return render(request, 'book_success.html')

#HTML-форма отправляет данные через GET или POST,
# а Django принимает их через ContactForm(request.POST) и проверяет через form.is_valid()