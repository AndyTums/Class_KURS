class Vacancies:
    """ Класс для работы с вакансиями. Включает в себя сортировку необходимых данных из списка словарей
                        и добавления их в список, а также сравнение двух вакансий по ЗП """

    def __init__(self, name: str, description: str, url: str, salary_from,
                 salary_to):
        self.name = name
        self.description = description
        self.url = url
        if isinstance(salary_from, int):
            self.salary_from = salary_from
        else:
            self.salary_from = 0
        if isinstance(salary_to, int):
            self.salary_to = salary_to
        else:
            self.salary_to = 0

    @classmethod
    def cast_to_object_list(cls, info_list: list):
        """ Класс метод принимает список словарей с вакансиями, отбирает необходимы данные
                                и добавляет классовым объектом в список """

        list_vacancies = []
        for i in info_list:
            name = i["name"]
            description = i["snippet"]["responsibility"]
            if i["salary"]:
                if i["salary"]["from"]:
                    salary_from = i["salary"]["from"]
                else:
                    salary_from = 0
                if i["salary"]["to"]:
                    salary_to = i["salary"]["to"]
                else:
                    salary_to = 0
            url = i["area"]["url"]

            vacancy = cls(name=name, description=description, salary_from=salary_from, salary_to=salary_to, url=url)

            list_vacancies.append(vacancy)

        return list_vacancies

    def __lt__(self, other):
        """ Метод сравнение ЗП двух вакансий """

        return self.salary_from > other.salary_from
