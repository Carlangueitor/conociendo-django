from django import forms
from tweets.models import Tweet


class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        exclude = ('fecha_de_creacion', 'usuario')
