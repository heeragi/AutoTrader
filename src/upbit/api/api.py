import hashlib
import os
import uuid
from urllib.parse import unquote, urlencode

import jwt
import requests


class UpbitAPIBase:

    def __init__(self):
        self.__access_key = os.environ.get('UPBIT_API_ACCESS_KEY')
        self.__secret_key = os.environ.get('UPBIT_API_SECRET_KEY')
        self.__host = 'https://api.upbit.com/'


    def __get_token(self, payload):
        token = jwt.encode(payload, self.__secret_key)
        return f'Bearer {token}'

    def __get_headers(self, payload):
        return {'Authorization': self.__get_token(payload)}

    def __encrypt_querystring(self, params):
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")
        m = hashlib.sha512()
        m.update(query_string)
        return m.hexdigest()

    def __get_payload(self, params):
        payload = {
            'access_key': self.__access_key,
            'nonce': str(uuid.uuid4())
        }
        if params is not None:
            payload['query_hash'] = self.__encrypt_querystring(params)
            payload['query_hash_alg'] = 'SHA512'
        return payload

    def _call_api(self, method: str, path: str, params=None):

        if method not in ['GET', 'POST', 'PUT', 'DELETE']:
            raise ValueError('HTTP 메소드를 확인해 주시기 바랍니다.')

        if path == '' or path is None:
            raise ValueError('Path must not be empty')

        headers = self.__get_headers(self.__get_payload(params))

        response = requests.request(
            method=method,
            url=f'{self.__host}/{path}',
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            raise Exception(response.text)

        if response is None:
            raise Exception('API Error')

        return response.json()

    def _mapping_list(self, instance, results):
        return list(map(lambda x: instance.model_validate(x), results))


