from api import PetFriends
from typing import Union
import settings as s

pf = PetFriends()
_, key = pf.get_api_key(s.email, s.password)
_, my_pets = pf.get_pets(key['key'], 'my_pets')
_, delete = pf.del_pet(key['key'], my_pets['pets'][0]['id'])

