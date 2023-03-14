import json
import time

import variables
import requests
from requests.auth import HTTPBasicAuth
import robot
from robot.utils import DotDict


def authenticate():
    auth = HTTPBasicAuth(variables.APP_ID, variables.APP_SECRET)
    data = {'grant_type': 'password',
            'username': variables.USERNAME,
            'password': variables.PASSWORD}
    _res = requests.post('https://www.reddit.com/api/v1/access_token',
                         auth=auth, data=data, headers=variables.headers)
    if 'access_token' not in _res.json():
        raise Exception('Access denied, check your app id/secret or login/password')
    variables.token = _res.json()['access_token']
    file = open('token', 'w')
    file.truncate(0)
    file.write(variables.token)
    file.close()


def set_token():
    file = open('token', 'r')
    variables.token = file.read()
    file.close()
    if len(variables.token) == 0:
        authenticate()


def api_request(method: str, params: dict = None) -> requests.Response:
    _res = requests.get(f'{variables.API_URL}{method}',
                        params=params,
                        headers=variables.headers)
    return _res


def api_request_post(method: str, params: dict = None) -> requests.Response:
    _res = requests.post(f'{variables.API_URL}{method}',
                         params=params,
                         headers=variables.headers)
    return _res


if __name__ == '__main__':
    variables.headers = {'User-Agent': 'LobaevScript'}
    set_token()
    variables.headers = {**variables.headers, **{'Authorization': f"bearer {variables.token}"}}

    variables.params_search = {'query': f'r/{variables.search_key}'}
    variables.params_comment = {'thing_id': f't3_{variables.POST_ID}',
                                'text': 'I LIKE PYTHON! WOW'}

    robot.run('TestCases/reddit.robot')
