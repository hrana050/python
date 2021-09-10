from django import forms 

class ImagefieldForm(forms.Form): 
    title = forms.CharField() 
    pic = forms.ImageField() 