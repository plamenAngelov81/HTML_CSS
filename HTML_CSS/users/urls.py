from django.urls import path

from HTML_CSS.users.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
]