from framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/category_list/': views.category_list,
    '/create_course/': views.create_course,
    '/create_category/': views.create_category,
}


def footer_controller(request):
    request['footer'] = \
        """
        <footer>
        <hr>
        <p>Все права защищены &copy;</p>
        </footer>
        """


front_controllers = [
    footer_controller
]


application = Application(urlpatterns, front_controllers)
