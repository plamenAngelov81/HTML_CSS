from django.views import generic


class HtmlStructureHome(generic.TemplateView):
    template_name = 'html_structure/structure_home.html'


class NavigationBar(generic.TemplateView):
    template_name = 'html_structure/navigation_bar.html'


class PageContent(generic.TemplateView):
    template_name = 'html_structure/page_content.html'


class SemanticTags(generic.TemplateView):
    template_name = 'html_structure/semantic_tags.html'


class SemanticArticlePage(generic.TemplateView):
    template_name = 'html_structure/semantic_article_page.html'


class SimpleWebSite(generic.TemplateView):
    template_name = 'html_structure/simple_web_site.html'


class SemanticBlogLayout(generic.TemplateView):
    template_name = 'html_structure/semantic_blog.html'
