import random

import pytest

from src.constants.votes_data import VotesData as VD
from src.utils import helpers
from src.utils import request


@pytest.fixture
def setup_create_vote():
    response = request.get_public_image()
    image_id = helpers.get_image_id(response)
    return image_id


@pytest.fixture()
def setup_delete_vote():
    response = request.get_public_image()
    image_id = helpers.get_image_id(response)
    response = request.send_vote(image_id=image_id)
    vote_id = helpers.get_vote_id(response)
    return vote_id


def test_vote_for_existing_image(setup_create_vote):
    image_id = setup_create_vote
    response = request.send_vote(image_id=image_id)

    # check vote is successful
    assert response.status_code == 200, 'Incorrect status code'
    assert response.json()['message'] == VD.SUCCESS_MESSAGE, 'Incorrect message in response'


def test_delete_existing_vote(setup_delete_vote):
    vote_id = setup_delete_vote
    response = request.delete_vote(vote_id=vote_id)

    # check delete is successful
    assert response.status_code == 200, 'Incorrect status code'
    assert response.json()['message'] == VD.SUCCESS_MESSAGE, 'Incorrect message in response'


def test_delete_non_existing_vote():
    response = request.delete_vote(vote_id=random.randint(1, 1000))

    # check non-existing delete vote handled correctly
    assert response.status_code == 400, 'Incorrect status code'
    assert response.json()['message'] == VD.WRONG_ACCOUNT_MESSAGE, 'Incorrect message in response'
