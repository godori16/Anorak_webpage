from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class IntroductionPageView(TemplateView):
    template_name = 'introduction.html'

class ProductPageView(TemplateView):
    template_name = 'product.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'