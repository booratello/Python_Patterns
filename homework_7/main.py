from framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/category_list/': views.CategoryListView(),
    '/create_course/': views.create_course,
    '/create_category/': views.CategoryCreateView(),
    '/create_student/': views.StudentCreateView(),
    '/student_list/': views.StudentListView(),
    '/add_student/': views.AddStudentByCourseCreateView(),
    '/api/': views.course_api,
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
