from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import ContentUsForm
from django.views import View


class ContactUsView(View):
    template_name = 'contact/contact-us.html'
    form_class = ContentUsForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been successfully sent.'), 'success')
            return redirect('ContactUs:contact_us')
        else:
            return render(request, self.template_name, {'form': form})
