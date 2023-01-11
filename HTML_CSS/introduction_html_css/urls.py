from django.urls import path

from HTML_CSS.introduction_html_css.views import Fruits, WikiPage, ToDoList, HtmlLists, DefinitionLists, \
    ReversedLists, ModernJS, BookStore, WorldCup, Welcome, HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
    path('welcome/', Welcome.as_view(), name='welcome'),
    path('fruit/', Fruits.as_view(), name='fruits'),
    path('wiki', WikiPage.as_view(), name='wiki'),
    path('to-do/', ToDoList.as_view(), name='to do'),
    path('html-list/', HtmlLists.as_view(), name='html list'),
    path('definition-lists/', DefinitionLists.as_view(), name='definition lists'),
    path('reversed/', ReversedLists.as_view(), name='reversed'),
    path('modern-js/', ModernJS.as_view(), name='modern'),
    path('book-story/', BookStore.as_view(), name='book story'),
    path('word-cup-news/', WorldCup.as_view(), name='news'),
]
