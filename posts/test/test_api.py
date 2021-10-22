import requests


class TestPosts:
    get_token_endpoint = 'http://127.0.0.1:8000/login/'
    credentials = {"username": "admin", "password": "admin"}
    user_token = requests.post(url=get_token_endpoint, data=credentials).json()['access']
    headers = {'Authorization': f'Bearer {user_token}'}
    endpoint_posts = 'http://127.0.0.1:8000/api/v1/posts/'

    def test_get_posts(self):
        posts = requests.get(url=self.endpoint_posts, headers=self.headers)
        assert posts.status_code == 200

    def test_get_post(self):
        post = requests.get(url=f'{self.endpoint_posts}16/', headers=self.headers)
        assert post.status_code == 200

    # def test_post_post(self):
    #     new_post = {
    #         "image": "posts/Screenshot_from_2021-07-11_18-34-44_KUQ1V95.png",
    #         "description": "description for new post"
    #     }
    #
    #     response = requests.post(url=self.endpoint_posts, headers=self.headers, data=new_post)
    #     assert response.status_code == 200

    def test_put_post(self):
        post_updated = {
            "image": "posts/Screenshot_from_2021-07-11_18-34-44_KUQ1V95.png",
            "description": "description for post updated"
        }

        response = requests.put(url=f'{self.endpoint_posts}6/', headers=self.headers, data=post_updated)
        assert response.status_code == 200

    def test_delete_post(self):
        response = requests.delete(url=f'{self.endpoint_posts}6/', headers=self.headers)
        assert response.status_code == 200
