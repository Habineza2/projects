from django.shortcuts import render
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')



from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm,LoginForm

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})




# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username").lower()
#         password = request.POST.get("password")

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, "User Not Found....")
#             return redirect("home")

#         if user is not None:
#             login(request, user)
#             return redirect("home")
#         else:
#             messages.error(request, "Username or Password does not match...")

#     return render(request, "login.html")




# from . import forms
# from django.views.generic.edit import FormView
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login



# class LoginView(FormView):
#     template_name = 'login.html'
#     form_class = forms.LoginForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             user = authenticate(request, username=email, password=password)

#             if user is not None:
#                 login(request, user)
#                 # Redirect to a success page or dashboard
#                 return redirect('user:home')
#             else:
#                 # Invalid login, show an error message
#                 form.add_error(None, 'Invalid login credentials. Please try again.')

#         return render(request, self.login.html, {'form': form})
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Provide your login template
    fields = ["email", "password"]

    def form_valid(self, form):
        response = super().form_valid(form)

        if not self.request.user.is_authenticated:
            # Redirect back to the login page with an error message
            return redirect('login')

        return response

    def get_success_url(self):
        return reverse_lazy('success')
    










#social-django




