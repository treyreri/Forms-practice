from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, min_length=2, required=True, label="Name", widget=forms.TextInput(
            attrs={ #использование widget.attrs для добавления CSS-классов и placeholder
                'class' : 'form-control' ,
                'placeholder' : 'Your name' }))

    email = forms.EmailField(
        required=True, label="Email" , widget=forms.EmailInput(
            attrs={
                'class' : 'form-control' ,
                'placeholder' : 'Your email' }))

    subject = forms.CharField(
            max_length=100, required=True, widget=forms.TextInput(
                attrs={
                    'class' : 'form-control' ,
                    'placeholder' : 'Subject' }))

    message = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'class' : 'form-control' ,
                    'placeholder' : 'Your message' }) , required=True, label="Message")
    

    subject = forms.CharField(max_length=100, required=True)

    def clean_email(self): #проверка email. Если написать test@mail.ru форма выведет ошибку
        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com') :
            raise forms.ValidationError('Please use a gmail address')
        return email

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        subject = cleaned_data.get('subject')

        if name and subject and name.lower() == subject.lower():
            raise forms.ValidationError("Name and subject cannot be the same")
        return cleaned_data #clean используется для проверки, которая зависит от нескольких полей


#создаем бук форм
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title' , 'author', 'price']