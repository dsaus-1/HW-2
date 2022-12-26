import json
import re


def sort_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        file_read = json.load(file)
        answer = sorted(file_read, key=lambda x: x.get('date') if x.get('date') != None else '', reverse=True)
        return answer

def print_data(data):

    for operation_number in range(0, 5):
        try:
            date = re.sub(r'(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d).(\d{6})', r'\3.\2.\1', data[operation_number].get('date'))
        except:
            date = ''
        try:
            description = data[operation_number].get('description')
        except:
            description = ''
        try:
            from_ = re.sub(r'(\d{4})(\d\d)(\d\d)(\d{4})(\d{4})', r'\1 \2** **** \5', data[operation_number].get('from'))
        except:
            from_ = 'Not found'
        try:
            to = re.sub(r'(\d{12,16})(\d{4})', r'**\2', data[operation_number].get('to'))
        except:
            to = 'Not found'
        try:
            cost = data[operation_number]['operationAmount'].get('amount')
        except:
            cost = 0
        try:
            currency = data[operation_number]['operationAmount']['currency'].get('name')
        except:
            currency = ''

        print(f'{date} {description}\n{from_} -> {to}\n{cost} {currency}\n')



if __name__ == '__main__':
    print_data(sort_file('operations.json'))
