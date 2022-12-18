import csv

class ReadItems:
    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.file, self.mode)
        return csv.DictReader(self.open_file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open_file.close()


def show_items(file):
    with ReadItems(file, 'r') as items:
        for item in items:
            print(item)

show_items('items.csv')

