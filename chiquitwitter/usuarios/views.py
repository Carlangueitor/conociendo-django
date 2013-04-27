from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def registro(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'registro.html', {'form': form})
