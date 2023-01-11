from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HTML_CSS.introduction_html_css.urls'))
]
