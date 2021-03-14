from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    return render(request,'first_app/homepage.html')



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="first_app/customer_register.html", context={"register_form":form})




def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="first_app/customer_login.html", context={"login_form":form})



def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")

# def form_view(request):
#     form = forms.RegisterForm()
#
#     if request.method == 'POST':
#         form =  forms.RegisterForm(request.POST)
#
#         #if form.is_valid():
#         #    print("Validation success")
#         #    print("NAME:"+ form.cleaned_data['name'])
#         #    print("EMAIL:"+ form.cleaned_data['email'])
#         #    print("TEXT:" +form.cleaned_data['text'])
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('homepage')
#
#     return render(request,'first_app/register.html',{'form':form})
