from django.urls import path, include

from HTML_CSS.html_structure.views import NavigationBar, HtmlStructureHome, PageContent, SemanticTags, \
    SemanticArticlePage, SimpleWebSite, SemanticBlogLayout

urlpatterns = [
    path('structure/', include([
        path('', HtmlStructureHome.as_view(), name='structure home'),
        path('navbar/', NavigationBar.as_view(), name='nav bar'),
        path('page-content/', PageContent.as_view(), name='page content'),
        path('semantic/', SemanticTags.as_view(), name='semantic'),
        path('semantic-article-page/', SemanticArticlePage.as_view(), name='semantic article page'),
        path('simple-web-site/', SimpleWebSite.as_view(), name='simple website'),
        path('semantic-blog/', SemanticBlogLayout.as_view(), name='semantic blog')
    ]))
]