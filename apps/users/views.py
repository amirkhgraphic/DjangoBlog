from django.contrib import messages
from django.views.generic.edit import FormView
from apps.users.forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        credentials = form.cleaned_data
        user = authenticate(email=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            user_ip = self.request.META.get('REMOTE_ADDR', None)
            warning_message = f"user (with IP: {user_ip}) tried to log in with wrong credentials"
            messages.add_message(self.request, messages.WARNING, warning_message)
            return HttpResponseRedirect(reverse_lazy('users:log-in'))
