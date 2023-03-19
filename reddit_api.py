import os
import requests
from requests.auth import HTTPBasicAuth

import keyring
from dotenv import load_dotenv

from variables import constants, params


def load_environ():
    dotenv_path = os.path.join(os.path.dirname(__file__), 'login.env')
    if os.path.exists(dotenv_path):
        return load_dotenv(dotenv_path)
    return False


def get_token(use_existing):
    # Просмотр сохранённого токена
    token = keyring.get_password(constants.USER_AGENT, 'user_token')
    if token is not None and use_existing:
        return token

    if load_environ():
        login_result = log_in(
            os.getenv('APP_ID'),
            os.getenv('APP_SECRET'),
            os.getenv('LOGIN'),
            os.getenv('PASSWORD'),
        )
        if login_result[0]:
            keyring.set_password(constants.USER_AGENT, 'user_token', login_result[1])
            return login_result[1]

    # Аутентификация
    while True:
        # Запрос данных
        print('Enter app ID:')
        app_id = input()
        print('Enter app secret:')
        app_secret = input()
        print('Enter login:')
        login = input()
        print('Enter password:')
        password = input()

        login_result = log_in(
            app_id,
            app_secret,
            login,
            password
        )
        if login_result[0]:
            break

    # Сохранение токена
    keyring.set_password(constants.USER_AGENT, 'user_token', login_result[1])
    return login_result[1]


def log_in(app_id, app_secret, login, password):
    auth = HTTPBasicAuth(app_id, app_secret)
    data = {'grant_type': 'password',
            'username': login,
            'password': password}
    response = requests.post('https://www.reddit.com/api/v1/access_token',
                             auth=auth, data=data, headers=params.get_headers(), timeout=5)
    if 'access_token' not in response.json():
        return False
    else:
        return True, response.json()['access_token']


def get_api_request(method: str, parameters: dict = None) -> requests.Response:
    res = requests.get(f'{constants.API_URL}{method}',
                       params=parameters,
                       headers=params.get_headers(),
                       timeout=5)
    return res


def post_api_request(method: str, parameters: dict = None) -> requests.Response:
    res = requests.post(f'{constants.API_URL}{method}',
                        params=parameters,
                        headers=params.get_headers(),
                        timeout=5)
    return res
