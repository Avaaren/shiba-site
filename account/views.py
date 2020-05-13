from django.views.generic import CreateView

from .forms import RegistrationForm

class SignupView(CreateView):

    template_name = 'account/registration.html'
    form_class = RegistrationForm
    # success_url = reverse_lazy('account:signup-done')

    def form_valid(self, form):

        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['repeat_password'])
        new_user.save()

        return super().form_valid(form)


    
