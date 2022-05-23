import jsonschema
import json
import os

from py.path import local

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


def validate_json(response, schema):
    jsonschema.validate(instance=response.json(), schema=schema)
    return True


def get_json_schema(schema=""):
    project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))))
    configs_path = project_path.join("data")
    path = configs_path.join(f"{schema}_schema.json").strpath
    with open(path) as file:
        data = json.load(file) or {}
    return data