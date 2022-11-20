import unittest
from parameterized import parameterized, parameterized_class
from main import search_id, search_city, search_pop_site
from yandex import YandexDisk

ids = [
    ( {'user1': [0, 35, 213, 15, 35],
       'user2': [0, 54, 35, 119, 119],
       'user3': [35, 0, 98, 35] }, [0, 35, 213 , 15, 54, 119, 98]
     ) ,
    ( {'user1': [0, 0, 0, 0, 0],
       'user2': [0, 1, 0, 0, 0] }, [0 , 1], 
    )
]

country = [
            ( 'Португалия' ),
            ( 'Франция' ),
            ( 'Индия' )            
           ]

stats = [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
        ({'vk':1, 'ok': 300, 'fb': 98}, 'ok'),
        ({'facebook': 500, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook')
         ]
folder = [
        ( 'List' , 201 ),
        ( 'New' , 201)
          ]
access_token_ya = ''
ya = YandexDisk(token=access_token_ya)

class TestFunc(unittest.TestCase):
    @parameterized.expand(ids)
    def test_search_id(self,a, etalon ):
        self.assertEqual(search_id(a), etalon )
    
    @parameterized.expand(country)
    def test_search_city(self, a ):
        self.assert_(search_city(a))
    
    @parameterized.expand(stats)
    def test_search_pop_site(self, a, b):
        self.assertEqual(search_pop_site(a), b)
    
    @parameterized.expand(folder)
    def test_api(self, a, b):
        self.assertEqual(ya.create_folder(a) , b)
       
    @parameterized.expand(folder)
    def test_delete_folder(self,a, b):
        self.assertEqual(ya.delete_folder(a) , 204)