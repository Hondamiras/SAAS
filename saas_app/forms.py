from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#222]',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#222]',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#222]',
        'rows': 4
    }))
