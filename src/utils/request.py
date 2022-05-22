import requests

from src.utils.settings_parser import settings

base_url = settings.base_url
api_key = settings.api_key
user_agent = settings.user_agent

HEADERS = {
    'user-agent': user_agent,
    'x-api-key': api_key, 'Content-type': 'application/json', 'Accept': 'text/plain'}


def send_request(method, endpoint, headers=HEADERS, payload=None):
    url = base_url + endpoint
    if method == 'GET':
        response = requests.get(url, headers=headers)
        return response
    if method == 'POST':
        response = requests.post(url, headers=headers, json=payload)
        return response
    if method == 'DELETE':
        response = requests.delete(url, headers=headers)
        return response

    raise Exception('Method not found: ' + method)


def send_vote(image_id=None):
    payload = {
        'image_id': image_id,
        'value': 1
    }
    response = send_request(method='POST', endpoint="/votes/", payload=payload)
    return response


def get_categories():
    response = send_request(method='GET', endpoint="/categories")
    return response


def get_specific_vote(vote_id=None):
    response = send_request(method='GET', endpoint=f"/votes/{vote_id}")
    return response


def get_public_image():
    response = send_request(method="GET", endpoint="/images/search")
    return response


def delete_vote(vote_id=None):
    response = send_request(method='DELETE', endpoint=f"/votes/{vote_id}")
    return response
