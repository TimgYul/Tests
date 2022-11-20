import requests
import json


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        } 
    
    def create_folder(self, folder):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': f'{folder}', 'overwrite': 'false'}
        response = requests.api.put(url=url, headers=headers, params=params)
        return response.status_code
    
    def delete_folder(self, folder):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': f'{folder}', 'overwrite': 'false'}
        response = requests.api.delete(url=url, headers=headers, params=params)
        return response.status_code