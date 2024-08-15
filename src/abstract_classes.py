from abc import ABC, abstractmethod


class GetAPI(ABC):
    """ Абстрактный класс для работы API сервиса с вакансиями """

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
