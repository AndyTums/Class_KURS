import json

from src.abstract_classes import WorkJSON
from src.work_with_API import HeadHunter
from src.work_with_vacancies import Vacancies


class JSONSaver(WorkJSON):
    """ Класс для работы с файлами, а именно: записи, чтения и удаления информации по вакансиям """

    def __init__(self, filepath: str = "../data/vacancies.json"):
        self._filepath = filepath

    def add_in_file(self, info):
        """ Метод добавление информации в файл """

        with open(self._filepath, "w") as file:
            json.dump(info, file)

    def read_file(self):
        """ Метод чтения информации из файла """
        pass

    def del_from_file(self):
        """ Метод удаления информации из файла """
        pass


head = HeadHunter()
work = HeadHunter.get_info(head)
info = Vacancies.cast_to_object_list(work)  # список вакансий
print(info)

js = JSONSaver()
js.add_in_file(info)

