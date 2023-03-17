import requests
from requests.auth import HTTPBasicAuth
import keyring
import variables


def authenticate():
    _response = requests.Response
    # Сообщаем в заголовке о типе нашей программы
    variables.headers = {'User-Agent': variables.USER_AGENT}

    # Просмотр сохранённого токена
    _token = keyring.get_password(variables.USER_AGENT, 'user_token')
    if _token is not None:
        print('Token found. Enter with an existing account? Y/N')
        while True:
            _c = input()
            if _c in 'yY':
                variables.headers = {**variables.headers, **{'Authorization': f"bearer {_token}"}}
                return
            elif _c in 'nN':
                break
            else:
                print('Input Y or N!')

    # Аутентификация
    while True:
        # Запрос данных
        print('Enter app ID:')
        _app_id = input()
        print('Enter app secret:')
        _app_secret = input()
        print('Enter login:')
        _login = input()
        print('Enter password:')
        _password = input()

        _auth = HTTPBasicAuth(_app_id, _app_secret)
        _data = {'grant_type': 'password',
                 'username': _login,
                 'password': _password}
        _response = requests.post('https://www.reddit.com/api/v1/access_token',
                                  auth=_auth, data=_data, headers=variables.headers)
        if 'access_token' not in _response.json():
            print('Access denied, check your app id/secret or login/password')
        else:
            break
    _token = _response.json()['access_token']

    # Сохранение токена
    keyring.set_password(variables.USER_AGENT, 'user_token', _token)

    # Добавляем в заголовок наш токен
    variables.headers = {**variables.headers, **{'Authorization': f"bearer {_token}"}}


def get_api_request(method: str, params: dict = None) -> requests.Response:
    _res = requests.get(f'{variables.API_URL}{method}',
                        params=params,
                        headers=variables.headers)
    return _res


def post_api_request(method: str, params: dict = None) -> requests.Response:
    _res = requests.post(f'{variables.API_URL}{method}',
                         params=params,
                         headers=variables.headers)
    return _res
