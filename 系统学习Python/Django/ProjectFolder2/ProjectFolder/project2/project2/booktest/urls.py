from django.conf.urls import include,url
from booktest import views

urlpatterns = [
    url('^index/?$',views.show_books),
    url('^add/?$',views.add_book),
    url('^delete/([0-9]+)/?$',views.delete_book),
    url('^',views.show_books),
]