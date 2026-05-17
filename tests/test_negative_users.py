import pytest

def test_get_non_existing_user(api_client):
	response = api_client.get_user_by_id(9999)
	assert response.status_code == 404


def test_invalid_endpoint(api_client):
	response = api_client.get_invalid_endpoint()
	assert response.status_code == 404


@pytest.mark.parametrize("user_id",[9999,99999,0])
def test_negative_test_parametrized(api_client,user_id):
	response = api_client.get_user_by_id(user_id)
	assert response.status_code == 404