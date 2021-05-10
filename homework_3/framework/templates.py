"""
Работа с шаблонами, паттерн INTERFACE
Используем шаблонизатор jinja2
"""

from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры
    :return:
    """

    env = Environment()
    env.loader = FileSystemLoader(folder)
    # file_path = os.path.join(folder, template_name)
    template = env.get_template(template_name)
    return template.render(**kwargs)
