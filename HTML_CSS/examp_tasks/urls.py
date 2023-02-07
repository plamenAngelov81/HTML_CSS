from django.urls import path, include

from HTML_CSS.examp_tasks.views import TaskOneHomeView, RegistrationFormView, MaineHomeView, SignUpFormView, KiwiView, \
    FinancialServicesView, EnterpriseView, AutoView, MediumView, SimpleArticleView, RestaurantView, EarthView, \
    AdvantagesView, LoginTaskView

urlpatterns = [
    path('exams/', include([
        path('task-1/', include([
            path('', TaskOneHomeView.as_view(), name='task1 home'),
            path('registration-form/', RegistrationFormView.as_view(), name='registration form'),
            path('maine-home/', MaineHomeView.as_view(), name='maine home'),
            path('sign-up/', SignUpFormView.as_view(), name='sign up'),
            path('kiwi/', KiwiView.as_view(), name='kiwi'),
            path('financial-services', FinancialServicesView.as_view(), name='financial services'),
            path('enterprise/', EnterpriseView.as_view(), name='enterprise'),
            path('auto/', AutoView.as_view(), name='auto'),
            path('medium/', MediumView.as_view(), name='medium'),
            path('simple article/', SimpleArticleView.as_view(), name='simple article'),
            path('restaurant/', RestaurantView.as_view(), name='restaurant'),
            path('earth/', EarthView.as_view(), name='earth'),
            path('advantages/', AdvantagesView.as_view(), name='advantages'),
            path('login/', LoginTaskView.as_view(), name='login'),
        ]))
    ]))
]