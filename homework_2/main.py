from framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/businka/': views.businka_view,
    '/sith/': views.sith_view,
    '/keks/': views.keks_view,
    '/contact/': views.contact_view,
}


def footer_controller(request):
    request['footer'] = \
        """
        <footer>
        <h3><a href='/'>На главную</a></h3>
        <h3><a href=/businka/>Бусинка</a></h3>
        <h3><a href=/sith/>Ситх</a></h3>
        <h3><a href=/keks/>Кекс</a></h3>
        <h3><a href=/contact/>Восхититься</a></h3>
        <hr>
        <p>Все права защищены &copy;</p>
        </footer>
        """


front_controllers = [
    footer_controller
]

application = Application(urlpatterns, front_controllers)
