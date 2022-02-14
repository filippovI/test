from api import PetFriends
import settings as s

pf = PetFriends()

_, key = pf.get_api_key(s.email, s.password)
status, result = pf.del_pet(key['key'], 'jhgjkl')

print(status, result)
