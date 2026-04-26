import requests

class APIClient:
	def __init__(self,url):
		self.url = url

	def get_users(self):
		return requests.get(f"{self.url}/users")

	def create_user(self,payload):
		return requests.post(f"{self.url}/users", json=payload)

	def get_user_by_id(self,user_id):
		return requests.get(f"{self.url}/users/{user_id}")

	def delete_user(self,user_id):
		return requests.delete(f"{self.url}/users/{user_id}")

	def update_user(self,user_id,payload):
		return requests.put(f"{self.url}/users/{user_id}", json= payload)

	def patch_user(self,user_id,payload):
		return requests.patch(f"{self.url}/users/{user_id}", json=payload)
