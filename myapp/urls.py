from django.urls import path
from .views import vote_view
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('vote/', vote_view, name='vote'),
]