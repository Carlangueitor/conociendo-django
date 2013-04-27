from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from tweets.forms import TweetForm
from tweets.models import Tweet


@login_required
def nuevo_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.usuario = request.user
            tweet.save()
    form = TweetForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('nuevo-tweet.html', context)


def lista_tweets(request):
    tweets = Tweet.objects.all().order_by('-fecha_de_creacion')
    return render(request, 'listado.html', {'tweets': tweets})
