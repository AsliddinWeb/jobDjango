from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birth_day', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "Qisqacha ma'lumot kiriting. . "
                }
            ),
            'birth_day': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'required': True
                }
            ),
            'profile_picture': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*',
                    'required': True
                }
            )
        }
        labels = {
            'bio': 'Men haqimda',
            'birth_day': "Tug'ilgan sana",
            'profile_picture': "Rasm"
        }
