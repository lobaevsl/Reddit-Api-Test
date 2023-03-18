import requests
from requests.auth import HTTPBasicAuth
import keyring
from variables import constants, params


def authenticate():
    # Просмотр сохранённого токена
    token = keyring.get_password(constants.USER_AGENT, 'user_token')
    if token is not None:
        print('Token found. Enter with an existing account? Y/N')
        while True:
            _c = input()
            if _c not in ('y', 'Y', 'n', 'N'):
                print('Enter Y or N!')
                continue
            if _c in ('y', 'Y'):
                return token
            if _c in ('n', 'N'):
                break

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

        auth = HTTPBasicAuth(app_id, app_secret)
        data = {'grant_type': 'password',
                'username': login,
                'password': password}
        response = requests.post('https://www.reddit.com/api/v1/access_token',
                                 auth=auth, data=data, headers=params.get_headers(), timeout=5)
        if 'access_token' not in response.json():
            print('Access denied, check your app id/secret or login/password')
        else:
            break
    params.token = response.json()['access_token']

    # Сохранение токена
    keyring.set_password(constants.USER_AGENT, 'user_token', params.token)

    return params.token


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
