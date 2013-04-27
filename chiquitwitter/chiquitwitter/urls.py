from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from tweets.views import nuevo_tweet, lista_tweets
from usuarios.views import registro

urlpatterns = patterns('',
    url(r'^$', lista_tweets, name="lista_tweets"),
    url(r'^twittear/$', nuevo_tweet, name="nuevo_tweet"),
    url(r'^registro/$', registro, name="registro"),
    url(r'^login/$', 'django.contrib.auth.views.login', {"template_name": "registro.html"}, name="login"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
