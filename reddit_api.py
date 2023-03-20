import requests

from variables import constants, params, authorization


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
