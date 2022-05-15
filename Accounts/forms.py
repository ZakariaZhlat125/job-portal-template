from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from Accounts.models import User


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, *kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name :"
        self.fields['last_name'].label = "Last Name :"
        self.fields['email'].label = "Email :"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = " Confirm Password"
        self.fields['gender'].label = "Gender"
        self.fields['phone'].label = "Phone"
        self.fields['date_of_birth'].label = "Date Of Birth"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['phone'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone',
            }
        )
        self.fields['date_of_birth'].widget.attrs.update(
            {
                'placeholder': 'Enter Date Of Birth',
            }

        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'password1', 'password2', 'gender', 'date_of_birth']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=False)
        user.role = "user"
        if commit:
            user.save()
        return user


class CompanyRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, *kwargs)
        self.fields['first_name'].label = "First Name :"
        self.fields['last_name'].label = "Last Name :"
        self.fields['email'].label = "Email :"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = " Confirm Password"
        self.fields['phone'].label = "Phone"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['phone'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'password1', 'password2']

    def save(self, commit=True):

        user = UserCreationForm.save(self, commit=False)
        user.role = "user"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', })
    )
    password = forms.CharField(
        strip=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password', }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Password is not Match")

            if not user.is_active:
                raise forms.ValidationError("User is not Active")
        return super(UserLoginForm, self).clean(**args, **kwargs)

    def get_user(self):
        return self.user


class UserProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )

        class Meta:
            model = User
            fields = ["first_name", "last_name", "gender"]
