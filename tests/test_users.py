import pytest



def test_get_users(api_client):
	response = api_client.get_users()
	assert response.status_code == 200
	assert response.json()[0]["name"]
	assert len(response.json())> 0

	print(response.json()[0])
	print(response.json()[0]["name"])


def test_create_user(api_client):
    payload = {
        "name": "Denisa",
        "job": "QA"
    }
    response = api_client.create_user(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Denisa"
    assert response.json()["job"] == "QA"


def test_get_single_user(api_client):
    response = api_client.get_user_by_id(1)
    assert response.status_code == 200


def test_delete_user(api_client):
	response = api_client.delete_user(1)
	assert response.status_code in [200, 204]



def test_update_user(api_client):
	payload = {"name": "Andreea",
			   "job": "QA"}
	response = api_client.update_user(1,payload)
	assert response.status_code == 200
	assert response.json()["name"] == "Andreea"
	assert response.json()["job"] == "QA"


def test_patch_user(api_client):
	payload = {"name": "Denisa"}
	response = api_client.patch_user(1,payload)
	assert response.status_code == 200
	assert response.json()["name"] == "Denisa"


@pytest.mark.parametrize("user_id", [1,2,3])
def test_get_users_parametrized(api_client,user_id):
	response = api_client.get_user_by_id(user_id)
	assert response.status_code == 200
	data = response.json()
	assert data["id"]==user_id
	assert "name" in data
	assert "email" in data




