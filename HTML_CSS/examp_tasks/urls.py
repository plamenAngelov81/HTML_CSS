from django.urls import path, include

from HTML_CSS.examp_tasks.views import JunExamHomeView, HomeTaskView

urlpatterns = [
    path('exams/', include([
        path('html-css-exam-26-jun-2022/', include([
            path('', JunExamHomeView.as_view(), name='26-jun-2022'),
            path('26-2022-task-1', HomeTaskView.as_view(), name='26-jun-2022-task-1'),
        ]))
    ]))
]