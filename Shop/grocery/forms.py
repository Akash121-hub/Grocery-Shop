from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# from django import forms

# creating a form  
class RegisterForm(forms.ModelForm):

#     username = forms.CharField(
#     required=False,
#     widget=forms.Textarea(
#         attrs={"placeholder": "Username",}
#     ),
# )
    username =  forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':' '}), help_text=" ")
    # help_texts = {
    #     'username': _('help text'),
    # }
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Email '}))
    
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields  = ['username','email', 'password']
        labels = {
            '': _(' '),
        }
       

