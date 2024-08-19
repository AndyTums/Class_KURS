import json
import os

from src.abstract_classes import WorkJSON


class JSONSaver(WorkJSON):
    """ Класс для работы с файлами, а именно: записи, чтения и удаления информации по вакансиям """

    def __init__(self, filepath: str = "../data/vacancies.json"):
        self.__filepath = filepath

    def add_in_file(self, info):
        """ Метод добавление информации в файл """

        if os.stat(self.__filepath).st_size == 0:  # Проверяем на пустоту

            with open(self.__filepath, 'w', encoding='utf-8') as file:  # Записываем, если пустой
                json.dump(info, file, ensure_ascii=False, indent=4)

        else:  # Перебираем новый список и сравниваем с записанным, чего нет добавляем
            read_info = self.read_file()
            for i in info:
                if i in read_info:
                    continue
                else:
                    read_info.append(i)

            with open(self.__filepath, 'w', encoding='utf-8') as file:  # Записываем измененный файл
                json.dump(read_info, file, ensure_ascii=False, indent=4)

    def read_file(self):
        """ Метод чтения информации из файла """

        if os.stat(self.__filepath).st_size == 0:  # Проверяем на пустоту файл
            return "Файл пуст!"

        else:  # Считываем в случае не пустого файла
            with open(self.__filepath, "r") as file:
                return json.load(file)

    def del_from_file(self):
        """ Метод удаления информации из файла """
        pass
