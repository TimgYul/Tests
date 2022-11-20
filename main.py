from pprint import pprint
from yandex import YandexDisk
import requests

ids = {'user1': [0, 35, 213, 15, 35],
       'user2': [0, 54, 35, 119, 119],
       'user3': [35, 0, 98, 35]}

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google':93, 'email': 42, 'ok': 98} 

def search_id(ids):
    result = []
    for id in ids.values():
        # result.extend(id)
        for value in id:
            if value not in result:
                result.append(value)
    # return list(set(result))
    return result

def search_city(country):
    result_list = []
    for visit in geo_logs:
        if country in list(visit.values())[0]:
            if list(visit.values())[0][0] not in result_list:  
                result_list.append(list(visit.values())[0][0])
    return result_list

def search_pop_site(stats):
    sorted_tuples = sorted(stats.items(), key=lambda item: item[1])
    sorted_stats = {k: v for k, v in sorted_tuples}
    return str(list(sorted_stats.keys())[-1])


# result_ids = search_id(ids)
# print(result_ids)

# result_city = search_city('Россия')
# pprint(result_city)

# pprint(search_pop_site(stats))

access_token_ya = 'y0_AgAAAAAA5PmBAADLWwAAAADUQl3JfnvvLRucSEKBnCSUGpSRp7EaJiE'
ya = YandexDisk(token=access_token_ya)
# ya.create_folder('New')



 




     