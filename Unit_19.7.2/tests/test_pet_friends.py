from api import PetFriends
import settings as s

pf = PetFriends()


def test_get_api_key(email=s.email, password=s.password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_pets(flr=''):
    _, key = pf.get_api_key(s.email, s.password)
    status, result = pf.get_pets(key['key'], flr)
    assert status == 200
    assert len(result['pets']) > 0
