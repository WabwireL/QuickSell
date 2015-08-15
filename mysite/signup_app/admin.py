from django.contrib import admin
from .forms import Signupform
from .models import signup
class Signupadmin(admin.ModelAdmin):
	form = Signupform
	class Meta:
		model=signup

admin.site.register(signup, Signupadmin)