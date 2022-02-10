from api import PetFriends
import settings as s

pf = PetFriends()
_, key = pf.get_api_key(s.email, s.password)
_, add_pet = pf.add_pet('Котэ', 'cat', '22', key['key'], 'tests/images/cat.jpg')
