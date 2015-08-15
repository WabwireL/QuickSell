from django.shortcuts import render

from .models import signup

from .forms import Signupform, Loginform
def register(request):
    
    #if request.method== "POST":
    form1 = Signupform(request.POST )
    	    	
    #users = signup.objects.all()
    if form1.is_valid():
        saveform=form1.save(commit=False)
        saveform.save()
        #return render(request, 'signup_app/home.html')
    else:
        form1 = Signupform()
    	print "not valid"
    	#return render(request, 'signup_app/home.html')

    return render(request, 'signup_app/signup.html', {'form1': form1})
def home(request):
	#form1 = Signupform(request.POST or None)

	form = Loginform(request.GET )
	# if form.is_valid():
	# 	form1 = Signupform(request.POST or None)
	# 	return render(request, 'signup_app/signup.html', {'form1': form1})
        #return render(re
	return render(request, 'signup_app/home.html',{'form': form})
