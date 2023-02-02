from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HTML_CSS.introduction_html_css.urls')),
    path('', include('HTML_CSS.users.urls')),
    path('', include('HTML_CSS.html_structure.urls')),
    path('', include('HTML_CSS.css_typography.urls')),
    path('', include('HTML_CSS.css_box_model.urls')),
    path('', include('HTML_CSS.examp_tasks.urls')),
]
