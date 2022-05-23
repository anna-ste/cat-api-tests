from src.constants.categories_data import CategoriesData as CD
from src.utils import response_handler, request, schema_loader


def test_category_in_the_list():
    response = request.get_categories()

    # check existing category is in the list of categories
    assert response.status_code == 200, 'Incorrect status code'
    categories_names = response_handler.get_list_category_names(response)
    assert CD.EXISTING_CATEGORY in categories_names


def test_category_not_in_the_list():
    response = request.get_categories()

    # check existing category is not in the list of categories
    assert response.status_code == 200, 'Incorrect status code'
    categories_names = response_handler.get_list_category_names(response)
    assert CD.NON_EXISTING_CATEGORY not in categories_names


def test_category_list_json_schema():
    schema = schema_loader.get_json_schema(schema="category_list")
    response = request.get_categories()

    # check response corresponds to schema
    assert response_handler.validate_json(response, schema), 'Category list schema is not valid'

