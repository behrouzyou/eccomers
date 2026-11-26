from django import forms

from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password','class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password'
        }))

    class Meta:
        model = Account
        fields = ['first_name','last_name', 'email', 'password','phone_number']  # noqa: RUF012
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        confirm_password = cleaned_data.get('confirm_password')
        password = self.cleaned_data['password']
        
        if confirm_password != password:
            raise forms.ValidationError(
                'Passwords do not match. Please try again.')

            