from django.views import generic


class HomePage(generic.TemplateView):
    template_name = 'users/home_page.html'
