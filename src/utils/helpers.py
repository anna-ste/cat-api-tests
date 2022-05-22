def get_list_category_names(response):
    ids = list()
    if response:
        ids = [item['name'] for item in response.json()]
    return ids


def get_image_id(response):
    image_id = None
    if response:
        image_id = response.json()[0]['id']
    return image_id


def get_vote_id(response):
    vote_id = None
    if response:
        vote_id = response.json()['id']
    return vote_id
