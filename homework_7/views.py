from framework import render
from models import TrainingSite, BaseSerializer, EmailNotifier, SmsNotifier
from logging_mod import Logger, debug
from framework.frameworkcbv import ListView, CreateView
from frameworkorm import UnitOfWork
from mappers import MapperRegistry


site = TrainingSite()
logger = Logger('file')
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)


@debug
def main_view(request):
    logger.log('Список курсов')
    return '200 OK', render('course_list.html', objects_list=site.courses)


@debug
def category_list(request):
    logger.log('Список категорий')
    return '200 OK', render('category_list.html', objects_list=site.categories)


@debug
def create_course(request):
    if request['method'] == 'POST':
        # метод пост
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        # print(category_id)
        if category_id:
            category = site.find_category_by_id(int(category_id))

            course = site.create_course('record', name, category)
            # Добавляем наблюдателей на курс
            course.observers.append(email_notifier)
            course.observers.append(sms_notifier)
            site.courses.append(course)

        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories)
    else:
        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories)


# @debug
# def create_category(request):
#     if request['method'] == 'POST':
#         data = request['data']
#         name = data['name']
#         category_id = data.get('category_id')
#         category = None
#         if category_id:
#             category = site.find_category_by_id(int(category_id))
#         new_category = site.create_category(name, category)
#         site.categories.append(new_category)
#         # print(site.categories)
#         return '200 OK', render('create_category.html')
#     else:
#         categories = site.categories
#         return '200 OK', render('create_category.html', categories=categories)

@debug
class CategoryCreateView(CreateView):
    template_name = 'create_category.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context

    def create_obj(self, data: dict):
        name = data['name']
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)
        site.categories.append(new_category)


@debug
class CategoryListView(ListView):
    queryset = site.categories
    template_name = 'category_list.html'


@debug
class StudentListView(ListView):
    queryset = site.students
    template_name = 'student_list.html'

    def get_queryset(self):
        mapper = MapperRegistry.get_current_mapper('student')
        return mapper.all()

@debug
class StudentCreateView(CreateView):
    template_name = 'create_student.html'

    def create_obj(self, data: dict):
        name = data['name']
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)
        new_obj.mark_new()
        UnitOfWork.get_current().commit()

@debug
class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course = site.get_course(course_name)
        student_name = data['student_name']
        student = site.get_student(student_name)
        course.add_student(student)

@debug
def course_api(request):
    return '200 OK', BaseSerializer(site.courses).save()
