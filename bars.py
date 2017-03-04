import os
import sys
import json
import math


def get_file_path():
    return sys.argv[1] if len(sys.argv) > 1 else input('Введите путь к файлу .json : ')


def load_bars_from_file(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(list_bars):
    return None if not list_bars else max(list_bars, key=lambda x: x['SeatsCount'])


def get_smallest_bar(list_bars):
    return None if not list_bars else min(list_bars, key=lambda x: x['SeatsCount'])


def get_coordinates():
    try:
        longitude = float(input('Введите долготу: '))
        latitude = float(input('Введите широту: '))
        return longitude, latitude
    except ValueError:
        pass


def get_closest_bar(list_bars, coordinates):
    if not coordinates:
        return None
    return min(list_bars, key=lambda x: math.sqrt((float(x['geoData']['coordinates'][0]) - coordinates[0]) ** 2 +
                                                  (float(x['geoData']['coordinates'][1]) - coordinates[1]) ** 2))


if __name__ == '__main__':
    list_bars = load_bars_from_file(get_file_path())
    if list_bars is None:
        print('Нет такого файла "{0}"'.format(json_path))
        exit()

    biggest_bar = get_biggest_bar(list_bars)
    print('Ничего не найдено' if biggest_bar is None else
          'Самый большой бар "{0}", в нем {1} мест'.format(biggest_bar['Name'], biggest_bar['SeatsCount']))

    smallest_bar = get_smallest_bar(list_bars)
    print('Ничего не найдено' if smallest_bar is None else
          'Самый маленький бар "{0}", в нем {1} мест'.format(smallest_bar['Name'], smallest_bar['SeatsCount']))

    closest_bar = get_closest_bar(list_bars, get_coordinates())
    print('Ничего не найдено' if closest_bar is None else
          'Ближайший бар "{0}", координаты ({1}, {2})'
          .format(closest_bar['Name'], closest_bar['geoData']['coordinates'][0],
                  closest_bar['geoData']['coordinates'][1]))
