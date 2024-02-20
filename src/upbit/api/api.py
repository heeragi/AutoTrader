import os
import uuid

import jwt
import requests


class UpbitAPIBase:

    def __init__(self):
        self.__access_key = os.environ.get('UPBIT_API_ACCESS_KEY')
        self.__secret_key = os.environ.get('UPBIT_API_SECRET_KEY')
        self.__host = 'https://api.upbit.com/'

    def __get_token(self):
        payload = {
            'access_key': self.__access_key,
            'nonce': str(uuid.uuid4())
        }
        token = jwt.encode(payload, self.__secret_key)
        return f'Bearer {token}'

    def _call_api(self, method, path, params=None):
        url = f'{self.__host}/{path}'
        headers = {'Authorization': self.__get_token()}
        response = None

        if method == 'GET':
            response = requests.get(url, params=params, headers=headers)
        elif method == 'POST':
            response = requests.post(url, params=params, headers=headers)

        if response.status_code != 200:
            raise Exception(response.text)

        if response is None:
            raise Exception('API Error')

        return response.json()

    def _mapping_list(self, instance, results):
        return list(map(lambda x: instance.model_validate(x), results))


