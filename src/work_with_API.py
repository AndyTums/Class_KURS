import requests

from src.abstract_classes import GetAPI


class HeadHunter(GetAPI):
    """ Клас наследуется от абстрактного класса для работы с площадкой HeadHunter. """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': "", "page": 0, "per_page": 100}
        self.__code_status = requests.get(self.__url).status_code
        self.__vacancies = []

    def get_info(self):
        """ Метод для подключения к API и получение данных """
        if self.__code_status != 200:
            raise NameError(f"Не возможно получить данные, ошибка: Код {self.code_status}")

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


# if __name__ == "__main__":
#
#     head = HeadHunter()
#     # print(head.get_info())
#     print(head.get_vacancies("курьер"))
#
#     # url = "https://api.hh.ru/vacancies"
#     # response = requests.get(url)
#     # print(response.json()["items"])
