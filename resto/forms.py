from django import forms
from django.contrib.auth import authenticate, get_user_model, login,logout
from .models import Foodcort
User = get_user_model()

class UserRestoLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if username and password:
            if not user:
                raise forms.ValidationError("user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("incorrect password")
            if not user.is_active:
                raise forms.ValidationError("user not valid")
        return super(UserRestoLoginForm,self).clean(*args,**kwargs)

class UserRestoRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'password',
            ]



class RestoDashForm(forms.ModelForm):
    class Meta:
        model = Foodcort
        fields = ['resto_name','product_name','product_cuisines','product_img','product_about','product_price']
