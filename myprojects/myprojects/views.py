

# from django.shortcuts import render
# from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html')

# def success(request):
#     return render(request, 'success.html')



# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from user.forms import SignupForm,LoginForm

# def register(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect('success')
#     else:
#         form = SignupForm()
#     return render(request, 'register.html', {'form': form})






# from user.models import CustomUser
# from codes.forms import CodeForm











# from django.urls import reverse_lazy
# from django.contrib.auth.views import LoginView
# class CustomLoginView(LoginView):
#     template_name = 'login.html'  # Provide your login template
#     fields = ["email", "password"]

#     def form_valid(self, form):
#         response = super().form_valid(form)

#         if not self.request.user.is_authenticated:
            
#             # Redirect back to the login page with an error message
#             return redirect('login')

#         return response

#     def get_success_url(self):
#         return reverse_lazy('verify')
    










# #social-django


# def verify(request):
#     form = CodeForm(request.POST or None)
#     pk=request.session.get('pk')
#     if pk:
#        user= CustomUser.objects.get(pk=pk)
#        code=user.code
#        code_user = f"{user.email}: {user. code}"
#        if not request.POST:
#         print(code_user)
        
#            #send sms
    
#         if form.is_valid():
#             num=form.cleaned_data.get('number')
#             if str(code) == num:
#                 code.save()
#                 login(request, user)
#                 return redirect(success)
#             else:
#                 return redirect(login)
#     return render(request, 'verify.html',{'form':form})        
            

