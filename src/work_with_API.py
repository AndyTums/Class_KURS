import requests

from src.abstract_classes import GetAPI


class HeadHunter(GetAPI):
    """ Клас наследуется от абстрактного класса для работы с площадкой HeadHunter.
        Включает в себя: получение информации всех вакансий, а по наименованию """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': "", "page": 0, "per_page": 100}
        self.__code_status = requests.get(self.__url).status_code

    def get_info(self):
        """ Метод для подключения к API и получение данных """

        if self.__code_status != 200:
            raise NameError(f"Не возможно получить данные, ошибка: Код {self.__code_status}")

        else:
            response = requests.get(self.__url, self.__params)
            return response.json()["items"]

    def get_vacancies(self, vacancies: str = None) -> list:
        """ Метод получающий информацию по заданной вакансии, в противном случае выводит все вакансии """

        if self.__code_status != 200:
            raise NameError(f"Не возможно получить данные, ошибка: Код {self.__code_status}")

        else:
            if vacancies is not None:
                self.__params = {'text': vacancies, "page": 0, "per_page": 100}
                response = requests.get(self.__url, self.__params)
                return response.json()["items"]
            else:
                return HeadHunter.get_info(self)
