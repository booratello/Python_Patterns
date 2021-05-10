from reusepatterns.singletones import SingletonByName
from time import time


class ConsoleWriter:

    def write(self, text):
        print(text)


class FileWriter:

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{text}\n')


class Logger(metaclass=SingletonByName):

    def __init__(self, writer='console', file_name='logfile.txt'):
        self.writer = ConsoleWriter() if writer != 'file' else FileWriter(file_name)
        self.file_name = file_name

    def log(self, text):
        text = f'log---> {text}'
        self.writer.write(text)


# декоратор
def debug(func):
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('DEBUG-------->', func.__name__, end - start)
        return result

    return inner
