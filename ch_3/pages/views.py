from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    # handles the Homepage view
    template_name = "pages/home.html"


class AboutView(TemplateView):
    # handles the About page view
    template_name = "pages/about.html"
