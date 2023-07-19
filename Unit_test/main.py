import pytest
import requests


class TestClassPets:

    @pytest.mark.api
    def test_getAllPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

    @pytest.mark.api
    def test_getMyPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/my_pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

    @pytest.mark.ui
    def test_anotherTestPets(self):
        pass
