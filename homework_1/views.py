from framework import render


def main_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('index.html', footer=footer)

def businka_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('Businka.html', footer=footer)

def sith_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('Sith.html', footer=footer)

def keks_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('Keks.html', footer=footer)
