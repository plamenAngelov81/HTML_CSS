from django.views import generic


class TaskOneHomeView(generic.TemplateView):
    template_name = 'exams/task_1/home_task_1.html'


class RegistrationFormView(generic.TemplateView):
    template_name = 'exams/task_1/registration_form.html'


class MaineHomeView(generic.TemplateView):
    template_name = 'exams/task_1/maine_home.html'


class SignUpFormView(generic.TemplateView):
    template_name = 'exams/task_1/sign_up_form.html'


class KiwiView(generic.TemplateView):
    template_name = 'exams/task_1/kiwi.html'


class FinancialServicesView(generic.TemplateView):
    template_name = 'exams/task_1/financial_services.html'


class EnterpriseView(generic.TemplateView):
    template_name = 'exams/task_1/enterprise.html'


class AutoView(generic.TemplateView):
    template_name = 'exams/task_1/auto.html'


class MediumView(generic.TemplateView):
    template_name = 'exams/task_1/medium.html'


class SimpleArticleView(generic.TemplateView):
    template_name = 'exams/task_1/simple_article.html'


class RestaurantView(generic.TemplateView):
    template_name = 'exams/task_1/restaurant.html'


class EarthView(generic.TemplateView):
    template_name = 'exams/task_1/earth.html'


class AdvantagesView(generic.TemplateView):
    template_name = 'exams/task_1/advantages.html'


class LoginTaskView(generic.TemplateView):
    template_name = 'exams/task_1/login.html'
