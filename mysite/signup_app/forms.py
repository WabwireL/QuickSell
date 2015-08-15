from django import forms
from .models import signup, Login

class Signupform(forms.ModelForm):

	class Meta:
		model=signup
		date_of_birth =forms.DateField(label='date_of_birth', input_formats=['%d/%m/%Y'], )
		widgets= {'password': forms.PasswordInput(),}
		fields='__all__'

class Loginform(forms.ModelForm):
	
	class Meta:
		model=Login
		widgets= {'password': forms.PasswordInput(),}
		fields='__all__'