import json


def load_data():
    entered = input('Enter filename, please?')
    data = open(entered, encoding='utf-8')
    json.load(data)
    print(data)


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    load_data()