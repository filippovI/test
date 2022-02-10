from api import PetFriends
import settings as s

pf = PetFriends()
_, key = pf.get_api_key(s.email, s.password)
_, my_pets = pf.get_pets(key['key'], 'my_pets')
status, my_del_pets = pf.del_pet(key['key'], my_pets['pets'][0]['id'])
print(status, my_del_pets)

