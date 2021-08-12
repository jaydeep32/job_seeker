from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from user.forms import LoginForm, RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.files import File
from user.models import Profile

# Create your views here.


class CustomeLogin(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('job:home')
        return super().dispatch(request, *args, **kwargs)
    

def custome_register(request):
    if request.user.is_authenticated:
        return redirect('job:home')
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
	    if form.is_valid():
		    form.save()
		    return redirect("user:login")
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)
    

@login_required
def profile(request):
    next_url = request.GET.get('next')
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(next_url)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'user/profile.html', context)
    

