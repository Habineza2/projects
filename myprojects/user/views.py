

import random
from django.shortcuts import render
from django.urls import reverse_lazy

from codes.models import Code

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')



from django.shortcuts import render, redirect
from django.contrib.auth import login
from user.forms import SignupForm,LoginForm

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('success')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})






from user.models import CustomUser
from codes.forms import CodeForm











from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Provide your login template
    fields = ["email", "password"]

    def form_valid(self, form):
        response = super().form_valid(form)

        if not self.request.user.is_authenticated:
            return redirect('login')
        else:
            verification_code = self.generate_verification_code()
            code_object, created = Code.objects.get_or_create(user=self.request.user)
            code_object.number = verification_code
            code_object.save()
            print(f"Verification code for user {self.request.user.email}: {verification_code}")

          


        return response

    def get_success_url(self):
        return reverse_lazy('verify')
    

    def generate_verification_code(self):
        number_list = [x for x in range(10)]
        code_items = [str(random.choice(number_list)) for _ in range(5)]
        return "".join(code_items)
    
    










#social-django



def verify(request):
    if request.method == 'POST':
        
        form = CodeForm(request.POST)
        pk = request.session.get('pk')
        
        if pk:
            user = CustomUser.objects.get(pk=pk)
            code = user.code
            print(f"Stored verification code for user {user.email}: {code.number}")
            
            if form.is_valid():
                num = form.cleaned_data.get('number')
                
                if str(code) == num:
                    
                    code.save()
                    login(request, user, backend = 'django.contrib.auth.backends.ModelBackend'
)
                    
                    return redirect('success')
                    
                else:
                    return redirect('login')  # Replace with your actual failure URL
                    
        return render(request, 'verify.html', {'form': form})
    else:
        form = CodeForm()
        return render(request, 'verify.html', {'form': form})
   
            

