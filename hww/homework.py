import os

class ChangeDir:
    def __init__(self, name_dir):
        self.start_dir = os.getcwd()
        self.name_dir = name_dir

    def __enter__(self):
        try:
            self.work_dir = os.chdir(self.name_dir)
            return self.work_dir
        except FileNotFoundError:
            print('Директория не найдена!\nВыберите директорию из списка и повторите запрос:', end=' ')

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.start_dir)


with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir3'):
    print(os.listdir())

# вывод в консоль
# ['log.txt']
# ['file1.py', 'file2.py']
