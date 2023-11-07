from django.shortcuts import render, get_object_or_404, redirect
from .models import Word
from .forms import WordForm


def search(request):
    query = request.GET.get('q', '').strip()
    if query:
        results = Word.objects.filter(word__istartswith=query)
        no_results = not results.exists()
        return render(request, 'search.html', {'results': results, 'query': query, 'no_results': no_results})
    else:
        return render(request, 'search.html', {'results': None, 'query': '', 'no_results': False})


def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save()
            return redirect('web:search')
    else:
        form = WordForm()
    return render(request, 'add_word.html', {'form': form })


def update_word(request, id):
    word = get_object_or_404(Word, pk=id)
    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save()
            return redirect('web:search')
    else:

        form = WordForm(instance=word)
    return render(request, 'update_word.html', {'form': form, 'word': word})


