import requests as rq
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.url = 'https://petfriends1.herokuapp.com/'

    def get_api_key(self, email: str, password: str) -> [int, str | dict]:
        headers = {
            'email': email,
            'password': password
        }
        res = rq.get(self.url + 'api/key', headers=headers)
        try:
            result = res.json()
        except:
            result = res.text
        return res.status_code, result

    def get_pets(self, key: str, flr: str = '') -> [int, str | dict]:
        headers = {'auth_key': key}
        flr = {'filter': flr}

        res = rq.get(self.url + 'api/pets', headers=headers, params=flr)
        try:
            result = res.json()
        except:
            result = res.text
        return res.status_code, result

    def add_pet(self, name: str, animal_type: str, age: str, key: str, pet_photo: str) -> [int, str | dict]:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'))
            })

        headers = {
            'auth_key': key,
            'Content-Type': data.content_type
        }

        res = rq.post(self.url + 'api/pets', headers=headers, data=data)
        try:
            result = res.json()
        except:
            result = res.text
        return res.status_code, result

    def del_pet(self, key: str, pet_id: str) -> [int, str | dict]:
        res = rq.delete(self.url + 'api/pets/{0}'.format(pet_id), headers={'auth_key': key})
        try:
            result = res.json()
        except:
            result = res.text
        return res.status_code, result
