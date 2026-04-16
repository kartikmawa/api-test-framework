import pytest
from utils.api_client import get_post
from utils.validators import validate_post_data

@pytest.fixture
def response(request):
    post_id= request.param
    return get_post(post_id)


@pytest.mark.parametrize("response,expected_code, post_id,expected_user_id",[(1,200,1,1),(2,200,2,1),(3,200,3,1),(200,404,200,12)], indirect = ["response"])
def test_get_post_status_and_data_validation(response,expected_code,post_id,expected_user_id):
    f"Running test for post_id={post_id}"
    assert response.status_code == expected_code, f"Expected status {expected_code}, but got {response.status_code} for post"
    if expected_code == 200:  # Validate response body only for success case
        data = response.json()
        validate_post_data(data,post_id,expected_user_id)    # Validate response body only for success case