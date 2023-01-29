from django.views import generic


class BoxModelHomeView(generic.TemplateView):
    template_name = 'css_box_model/box_model_home_page.html'


class BlockModelContainerView(generic.TemplateView):
    template_name = 'css_box_model/block_model_container.html'


class ScrollingArticleView(generic.TemplateView):
    template_name = 'css_box_model/scrolling_article.html'


class BrazilCoffeeView(generic.TemplateView):
    template_name = 'css_box_model/brazil_coffee.html'


class ArticleView(generic.TemplateView):
    template_name = 'css_box_model/article.html'


class BlogArticle(generic.TemplateView):
    template_name = 'css_box_model/blog_article.html'


class NavigationInlineBlockView(generic.TemplateView):
    template_name = 'css_box_model/navigation_inline_block.html'


class WebsiteView(generic.TemplateView):
    template_name = 'css_box_model/website.html'


class PhotoGallery(generic.TemplateView):
    template_name = 'css_box_model/photo_gallery.html'


class BlogLayout(generic.TemplateView):
    template_name = 'css_box_model/blog_layout.html'
