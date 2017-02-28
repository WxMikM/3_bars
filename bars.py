import os
import json
import math


def load_bars_from_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(list_bars):
    if not list_bars:
        return None
    biggest_bar_now = list_bars[0]
    for bar in list_bars:
        if int(biggest_bar_now['SeatsCount']) < int(bar['SeatsCount']):
            biggest_bar_now = bar

    return biggest_bar_now


def get_smallest_bar(list_bars):
    if not list_bars:
        return None
    smallest_bar_now = list_bars[0]
    for bar in list_bars:
        if int(bar['SeatsCount']) < int(smallest_bar_now['SeatsCount']):
            smallest_bar_now = bar

    return smallest_bar_now


def get_closest_bar(list_bars, longitude, latitude):
    if not list_bars or not longitude or not latitude:
        return None
    closest_bar_now = list_bars[0]
    min_distance_now = math.sqrt((float(list_bars[0]['geoData']['coordinates'][0]) - longitude) ** 2 +
                                 (float(list_bars[0]['geoData']['coordinates'][1]) - latitude) ** 2)
    for bar in list_bars:
        temp_distance = math.sqrt((float(bar['geoData']['coordinates'][0]) - longitude) ** 2 +
                                  (float(bar['geoData']['coordinates'][1]) - latitude) ** 2)
        if temp_distance < min_distance_now:
            closest_bar_now = bar
            min_distance_now = temp_distance

    return closest_bar_now


if __name__ == '__main__':
    list_bars = None

    while list_bars is None:
        file_path = input('Введите путь к файлу .json : ')
        list_bars = load_bars_from_file(file_path)
        if list_bars is None:
            print('Нет такого файла {0}'.format(file_path))
    
    biggest_bar = get_biggest_bar(list_bars)
    print('Ничего не найдено' if biggest_bar is None else
          'Самый большой бар "{0}", в нем {1} мест'.format(biggest_bar['Name'], biggest_bar['SeatsCount']))

    smallest_bar = get_smallest_bar(list_bars)
    print('Ничего не найдено' if smallest_bar is None else
          'Самый маленький бар "{0}", в нем {1} мест'.format(smallest_bar['Name'], smallest_bar['SeatsCount']))

    try:
        longitude = float(input('Введите долготу: '))
    except ValueError:
        longitude = None

    try:
        latitude = float(input('Введите широту: '))
    except ValueError:
        latitude = None

    closest_bar = get_closest_bar(list_bars, longitude, latitude)
    print('Ничего не найдено' if closest_bar is None else
          'Ближайший бар "{0}", координаты ({1}, {2})'
          .format(closest_bar['Name'], closest_bar['geoData']['coordinates'][0],
                  closest_bar['geoData']['coordinates'][1]))
