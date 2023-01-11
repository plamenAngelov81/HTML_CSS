from django.views import generic


class HomePage(generic.TemplateView):
    template_name = 'introduction/home_page.html'


class Welcome(generic.TemplateView):
    template_name = 'introduction/welcome.html'


class Fruits(generic.TemplateView):
    template_name = 'introduction/fruits.html'


class WikiPage(generic.TemplateView):
    template_name = 'introduction/wiki_page.html'


class ToDoList(generic.TemplateView):
    template_name = 'introduction/to-do-list.html'


class HtmlLists(generic.TemplateView):
    template_name = 'introduction/html-lists.html'


class WorldCup(generic.TemplateView):
    template_name = 'introduction/world-cup-news.html'


class DefinitionLists(generic.TemplateView):
    template_name = 'introduction/definition_lists.html'


class ReversedLists(generic.TemplateView):
    template_name = 'introduction/reversed_lists.html'


class ModernJS(generic.TemplateView):
    template_name = 'introduction/modern-javascript.html'


class BookStore(generic.TemplateView):
    template_name = 'introduction/book-story.html'
