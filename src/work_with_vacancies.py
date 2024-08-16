class Vacancies:
    """ Класс для работы с вакансиями. Включает в себя сортировку необходимых данных из списка словарей
                        и добавления их в список, а также сравнение двух вакансий по ЗП """

    # __slots__ = ("name", "description", "salary_from", "salary_to" "url")

    def __init__(self, name: str, description: str, url: str, salary_from: None = "ЗП не указана",
                 salary_to: None = "ЗП не указана"):
        self.name = name
        self.description = description
        self.url = url
        self.salary_from = salary_from
        if salary_from == 0:
            self.salary_from = "ЗП не указанна"
        self.salary_to = salary_to
        if salary_to == 0:
            self.salary_to = "ЗП не указанна"

    @classmethod
    def cast_to_object_list(cls, info: list):
        """ Класс метод принимает список словарей с вакансиями, отбирает необходимы данные
                                и добавляет классовым обектом в список """

        list_vacancies = []
        for i in info:
            name = i["name"]
            description = i["snippet"]["responsibility"]
            salary_from = i["salary"]["from"]
            salary_to = i["salary"]["to"]
            # price = f"{i["salary"]["from"]} - {i["salary"]["to"]}"
            url = i["area"]["url"]

            vacancy = cls(name=name, description=description, salary_from=salary_from, salary_to=salary_to, url=url)

            list_vacancies.append(vacancy)

            return list_vacancies

    def __lt__(self, other):
        """ Метод сравнение ЗП двух вакансий """

        if isinstance(self.salary_from, str) or isinstance(other.salary_from, str):
            return "В одной из вакансий не указанна ЗП, сравнение невозможно."

        return self.salary_from > other.salary_from


if __name__ == "__main__":
    answer = [{'id': '105832314', 'premium': False, 'name': 'Курьер - Сборщик', 'department': None, 'has_test': False,
               'response_letter_required': False,
               'area': {'id': '47', 'name': 'Кемерово', 'url': 'https://api.hh.ru/areas/47'},
               'salary': {'from': 69600, 'to': 128750, 'currency': 'RUR', 'gross': False},
               'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
               'sort_point_distance': None, 'published_at': '2024-08-15T09:04:14+0300',
               'created_at': '2024-08-15T09:04:14+0300', 'archived': False,
               'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=105832314',
               'show_logo_in_search': None, 'insider_interview': None,
               'url': 'https://api.hh.ru/vacancies/105832314?host=hh.ru',
               'alternate_url': 'https://hh.ru/vacancy/105832314',
               'relations': [],
               'employer': {'id': '8639172', 'name': 'Сервис+ служба доставки',
                            'url': 'https://api.hh.ru/employers/8639172',
                            'alternate_url': 'https://hh.ru/employer/8639172',
                            'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/6600306.png',
                                          '90': 'https://img.hhcdn.ru/employer-logo/6600305.png',
                                          'original': 'https://img.hhcdn.ru/employer-logo-original/1244969.png'},
                            'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=8639172',
                            'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Готовы работать и учиться новому. Ответственны, пунктуальны и доброжелательны. Желание работать и зарабатывать. Ответственность и пунктуальность. Опыт работы в логистических...',
            'responsibility': 'Доставлять - собирать заказы от интернет-магазинов. Использовать мобильное приложение для получения заказов и информации о маршруте или составе заказа.'},
               'contacts': None, 'schedule': {'id': 'flexible', 'name': 'Гибкий график'},
               'working_days': [{'id': 'only_saturday_and_sunday', 'name': 'Работа только по\xa0сб\xa0и\xa0вс'}],
               'working_time_intervals': [
                   {'id': 'from_four_to_six_hours_in_a_day',
                    'name': 'Можно работать сменами по\xa04–6 часов в\xa0день'}],
               'working_time_modes': [{'id': 'start_after_sixteen', 'name': 'Можно начинать работать после 16:00'}],
               'accept_temporary': True, 'professional_roles': [{'id': '58', 'name': 'Курьер'}],
               'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
               'employment': {'id': 'part', 'name': 'Частичная занятость'}, 'adv_response_url': None,
               'is_adv_vacancy': False, 'adv_context': None}]

    head = Vacancies("Курьер", "длялялляля", "aSSASASD", 1, 50000)
    head_1 = Vacancies("Курьер", "длялялляля", "ASDSADADSA", 0, 100000)
    print(head_1.salary_from)
    print(head.salary_from)
    # head = Vacancies.cast_to_object_list(answer)
    print(head.__lt__(head_1))
