from framework import render


def main_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('index.html', footer=footer, image='/static/koshaki.jpg')

def businka_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('Businka.html', footer=footer, image='/static/busja.jpg')

def sith_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('Sith.html', footer=footer)

def keks_view(request):
    footer = request.get('footer', None)
    return '200 OK', render('Keks.html', footer=footer)

def contact_view(request):
    footer = request.get('footer', None)
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Получено сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('contact.html', footer=footer)
    else:
        return '200 OK', render('contact.html', footer=footer)
