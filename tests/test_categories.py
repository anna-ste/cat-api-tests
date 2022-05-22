from src.constants.categories_data import CategoriesData as CD
from src.utils import helpers
from src.utils import request


def test_category_in_the_list():
    response = request.get_categories()

    # check existing category is in the list of categories
    assert response.status_code == 200, 'Incorrect status code'
    categories_names = helpers.get_list_category_names(response)
    assert CD.EXISTING_CATEGORY in categories_names


def test_category_not_in_the_list():
    response = request.get_categories()

    # check existing category is not in the list of categories
    assert response.status_code == 200, 'Incorrect status code'
    categories_names = helpers.get_list_category_names(response)
    assert CD.NON_EXISTING_CATEGORY not in categories_names
