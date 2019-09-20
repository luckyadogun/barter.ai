from django import forms
from users.models import User


class UserCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'id': 'confirm-password', 'placeholder': 'Confirm Password'}))
    agree = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'agree-term', 'id': 'agree-term'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'id': 'firstname', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'id': 'lastname', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'id': 'email', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input', 'id': 'password', 'placeholder': 'Password'}),
        }    

    def check_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm-password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords don't match! Try again."
            )
        return password

    def clean_checkbox(self):
        agree = self.cleaned_data.get('agree')

        if not agree:
            raise forms.ValidationError(
                "Failed! Agree to our Terms and Conditions to continue."
            )
        return agree


class LoginForm(forms.Form):
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'label-agree-term', 'id': 'agree-term'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100', 'id': 'email', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'id': 'password', 'placeholder': 'Password'}))

    def check_remember(self):
        remember_me = self.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session_set_expiry(0)

        return remember_me
