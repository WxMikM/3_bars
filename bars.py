import json
import math

my_path = './data-2897-2016-11-23.json'


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    return data


def get_biggest_bar(data):
    if not data:
        return "не найдено"
    sch = data[0]
    for el in data:
        if int(sch['SeatsCount']) < int(el['SeatsCount']):
            sch = el

    return '{0} : {1} мест'.format(sch['Name'], sch['SeatsCount'])


def get_smallest_bar(data):
    if not data:
        return "не найдено"
    sch = data[0]
    for el in data:
        if int(el['SeatsCount']) < int(sch['SeatsCount']):
            sch = el

    return '{0} : {1} мест'.format(sch['Name'], sch['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    if not data:
        return "не найдено"
    shc = data[0]
    shc_long = math.sqrt((float(data[0]['geoData']['coordinates'][0]) - longitude) ** 2 +
                         (float(data[0]['geoData']['coordinates'][1]) - latitude) ** 2)
    for el in data:
        temp = math.sqrt((float(el['geoData']['coordinates'][0]) - longitude) ** 2 +
                         (float(el['geoData']['coordinates'][1]) - latitude) ** 2)
        if temp < shc_long:
            shc = el
            shc_long = temp

    return '{0} : {1}, {2}'.format(shc['Name'], shc['geoData']['coordinates'][0], shc['geoData']['coordinates'][1])


if __name__ == '__main__':
    print(get_biggest_bar(load_data(my_path)))
    print(get_smallest_bar(load_data(my_path)))
    print(get_closest_bar(load_data(my_path), 37,55))
