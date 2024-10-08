from django.urls import path

from myportfolio.views import home_view, portfolio_detail


urlpatterns = [
    path('', home_view, name='home'),
    path('portfolio/', portfolio_detail, name='portfolio_detail'),
]
