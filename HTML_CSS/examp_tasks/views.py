from django.views import generic


class JunExamHomeView(generic.TemplateView):
    template_name = 'exams/HTML & CSS Exam - 26 Jun 2022/26_jun_2022_home_page.html'


class HomeTaskView(generic.TemplateView):
    template_name = 'exams/HTML & CSS Exam - 26 Jun 2022/home.html'

