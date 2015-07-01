from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'poll_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
]
