from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import UserProfile
from django.utils import timezone
from .forms import UserForm,ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.


class AboutPage(TemplateView):
    template_name = 'about.html'

class LogoutPage(TemplateView):
    template_name = 'registration/logout.html'

class UserList(ListView):
    model =UserProfile
    template_name = 'proapp/userlist.html'

    def get_queryset(self):
        sear = self.request.GET.get("searchbar")

        if sear==None:
            return UserProfile.objects.filter(dateOfBirth__lte=timezone.now())
        else:
            return UserProfile.objects.filter(Q(college__icontains = sear))

class UserDetail(DetailView):
    model = UserProfile

class UserCreate(LoginRequiredMixin,CreateView):

    login_url = '/login/'
    redirect_field_name = 'usersdetail'
    form_class = ProfileForm
    model = UserProfile


class UserUpdateView(LoginRequiredMixin,UpdateView):

    login_url = '/login/'
    redirect_field_name = 'usersdetail'
    form_class = ProfileForm
    model = UserProfile


class UserDeleteView(LoginRequiredMixin,DeleteView):

    model = UserProfile
    success_url = reverse_lazy('userslist')



def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() :
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            return redirect('loginpage')
    else:
        form = UserForm()

    return render(request, 'signup.html', {
               'form': form,
           })
