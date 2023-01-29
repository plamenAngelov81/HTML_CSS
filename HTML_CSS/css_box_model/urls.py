from django.urls import path, include

from HTML_CSS.css_box_model.views import BoxModelHomeView, BlockModelContainerView, ScrollingArticleView, \
    BrazilCoffeeView, ArticleView, BlogArticle, NavigationInlineBlockView, WebsiteView, PhotoGallery, BlogLayout

urlpatterns = [
    path('css-box-model/', include([
        path('', BoxModelHomeView.as_view(), name='box model home'),
        path('box-model-container/', BlockModelContainerView.as_view(), name='box model container'),
        path('scroling-article/', ScrollingArticleView.as_view(), name='scrolling article'),
        path('brazil-coffee/', BrazilCoffeeView.as_view(), name='brazil coffee'),
        path('article/', ArticleView.as_view(), name='article'),
        path('blog-article/', BlogArticle.as_view(), name='blog article'),
        path('navigation-inline-block/', NavigationInlineBlockView.as_view(), name='navigation inline block'),
        path('website/', WebsiteView.as_view(), name='website'),
        path('photp-gallery/', PhotoGallery.as_view(), name='photo gallery'),
        path('blog-layout/', BlogLayout.as_view(), name='blog layout'),
    ]))
]
