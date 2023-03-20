import os
import requests
from requests.auth import HTTPBasicAuth

from dotenv import load_dotenv

import constants


def load_environ():
    dotenv_path = os.path.join(os.path.dirname(__file__), '../login.env')
    if os.path.exists(dotenv_path):
        return load_dotenv(dotenv_path)
    return False


def get_token():
    if load_environ():
        login_result = login(
            os.getenv('APP_ID'),
            os.getenv('APP_SECRET'),
            os.getenv('USERNAME'),
            os.getenv('PASSWORD'),
        )
        if login_result[0]:
            return login_result[1]


def login(app_id, app_secret, username, password):
    auth = HTTPBasicAuth(app_id, app_secret)
    data = {'grant_type': 'password',
            'username': username,
            'password': password}
    response = requests.post('https://www.reddit.com/api/v1/access_token',
                             auth=auth,
                             data=data,
                             headers={'User-Agent': constants.USER_AGENT},
                             timeout=5)
    if 'access_token' not in response.json():
        return False
    else:
        return True, response.json()['access_token']
