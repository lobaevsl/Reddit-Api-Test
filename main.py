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
    tkn = file.read()
    file.close()
    if len(tkn) == 0:
        authenticate()
    else:
        variables.token = tkn


def search(params: dict) -> requests.Response:
    _res = requests.get('https://oauth.reddit.com/api/search',
                        params=params,
                        headers=variables.headers)
    return _res


def api_request(method: str, params: dict) -> requests.Response:
    _res = requests.get(f'https://oauth.reddit.com/api/{method}',
                        params=params,
                        headers=variables.headers)
    return _res


if __name__ == '__main__':
    variables.headers = {'User-Agent': 'LobaevScript'}
    set_token()
    variables.headers = {**variables.headers, **{'Authorization': f"bearer {variables.token}"}}

    # robot.run('TestCases/reddit.robot')

