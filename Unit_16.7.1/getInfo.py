import requests as rq


class FromPetHouse:
    def __init__(self):
        self.__result_list = []

    def get_pets(self, type_list=None):
        if not type_list:
            type_list = ["cat"]
        # Сохраняем в переменную api для получения данных
        url_all_pets = "http://130.193.37.179/api/pet/?page=1&page_size=6"

        # Работаем с requests. Получаем данные и переводим их в json
        res = rq.get(url_all_pets)
        res_json = res.json()

        # Результат в виде словаря, включающим в себя спиок со словарями :)
        # Более детально это можно посмотреть во вкладке Response в DevTools
        # Перебираем список со словарями. Ищем нужные типы животных и заполняем рузультирующий лист
        for i in res_json["results"]:
            if (i["species"]["code"]) in type_list:
                self.__result_list.append(
                    {"type": i["species"]["name"], "name": i["name"], "gender": i["gender"]["name"], "age": i["age"]})

        # Функция изменения атрибутов питомцев. Если указан атрибут - меняем, иначе оставляем как было

    def set_value(self, pet_id=0, name=None, age=None, gender=None, pet_type=None):
        self.__result_list[pet_id]["name"] = name if name else self.__result_list[pet_id]["name"]
        self.__result_list[pet_id]["age"] = age if age else self.__result_list[pet_id]["age"]
        self.__result_list[pet_id]["gender"] = gender if gender else self.__result_list[pet_id]["gender"]
        self.__result_list[pet_id]["type"] = pet_type if pet_type else self.__result_list[pet_id]["type"]

        # Цикл вывода информации из result_list

    def show_pets(self):
        for i in self.__result_list:
            text_age = "лет"
            if i["age"] % 10 == 1:
                text_age = "год"
            elif 2 <= i["age"] % 10 <= 4:
                text_age = "года"
            print(f"{i['name']} ({i['type']}), {str(i['age'])} "
                  f"{text_age} - {i['gender']}. pet_id = {self.__result_list.index(i)}")

    # При необходимости удаления из памяти до окончания работы интерпретатора
    # def __del__(self):
    #     print('Список питомцев удален')