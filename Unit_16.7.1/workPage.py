from getInfo import FromPetHouse as fph

# Лист с типами животных
type_list = ["cat", "dog", "parrot"]

# Присваиваем pets класс FromPetHouse
pets = fph()

# Используем методы FromPetHouse
# getPets() - Получить животных с сайта. Принимает список с типами животных. По умолчанию - cat
# showPets()- Структурированно выводит информацию и полученных животных с их id в списке
# setValue(pet_id=0, name=None, age=None, gender=None, type=None)  - Позволяет менять атрибуты животных

# Примеры
pets.getPets(type_list)
pets.showPets()
print()
pets.setValue(name="Manny", age=3, pet_type="cow")
pets.showPets()
