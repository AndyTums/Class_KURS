from abc import ABC, abstractmethod


class GetAPI(ABC):
    """ Абстрактный класс для работы API сервиса с вакансиями """

    @abstractmethod
    def get_info(self):
        """ Абстрактный метод для подключения через API и получение информации """
        pass

    @abstractmethod
    def get_vacancies(self):
        """ Абстрактный метод для получения информации по вакансиям """
        pass


class WorkJSON(ABC):
    """ Абстрактный класс который включает в себя работу с файлами,
                а именно: добавления, чтение, удаления."""

    @abstractmethod
    def add_in_file(self, info):
        """ Абстрактный метод добавление информации в файл """
        pass

    @abstractmethod
    def read_file(self):
        """ Абстрактный метод чтения информации из файла """
        pass

    @abstractmethod
    def del_from_file(self):
        """ Абстрактный метод удаления информации из файла """
        pass
