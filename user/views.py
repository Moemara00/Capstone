from django.views.generic import CreateView , ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render,HttpResponse
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    queryset = User.objects.all()
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm

    def form_valid(self, form):

        messages.success(self.request,'Account Created Successfully')
        return super().form_valid(form)

def log_out(request):
    logout(request)
   
    return render(request,template_name="logout.html")