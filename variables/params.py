import variables.constants as constants

comment_id = ''


def get_headers(token: str = None):
    return {
        'User-Agent': constants.USER_AGENT,
        'Authorization': f'bearer {token}'
    }


def get_params_search_thread(query: str):
    return {
        'query': f'r/{query}'
    }


def get_params_add_comment(text: str = 'I LIKE PYTHON! WOW', post_id: str = constants.POST_ID):
    return {
        'thing_id': f't3_{post_id}',
        'text': text
    }


def get_comment_id():
    return comment_id


def set_comment_id(id: str):
    global comment_id
    comment_id = id
