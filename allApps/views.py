from django.shortcuts import render


def _render_page(request, template_name):
    return render(request, template_name)


def home(request):
    return _render_page(request, "index.html")


def about(request):
    return _render_page(request, "about.html")


def services(request):
    return _render_page(request, "services.html")


def team(request):
    return _render_page(request, "team.html")


def portfolio(request):
    return _render_page(request, "portfolio.html")


def portfolio_details(request):
    return _render_page(request, "portfolio-details.html")


def blog(request):
    return _render_page(request, "blog.html")


def blog_details(request):
    return _render_page(request, "blog-details.html")


def contact(request):
    return _render_page(request, "contact.html")
