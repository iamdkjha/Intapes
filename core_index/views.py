from django.shortcuts import render


def index(request):

    context = {
        'page_title': 'Intapes'
    }

    return render(request, 'index.html', context=context);