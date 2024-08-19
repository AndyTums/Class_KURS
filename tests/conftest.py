import pytest

from src.work_with_vacancies import Vacancies


@pytest.fixture
def info_api():
    return [{'id': '105832314', 'premium': False, 'name': 'Курьер - Сборщик', 'department': None, 'has_test': False,
             'response_letter_required': False,
             'area': {'id': '47', 'name': 'Кемерово', 'url': 'https://api.hh.ru/areas/47'},
             'salary': {'from': 0, 'to': None, 'currency': 'RUR', 'gross': False},
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


@pytest.fixture
def one_vacancy():
    return Vacancies("Курьер", "Доставка товара", "http://www.search.ru", 30000, 50000)


@pytest.fixture
def second_vacancy():
    return Vacancies("Повар", "Готовить еду", "http://www.kfc.ru", 50000, 85000)


@pytest.fixture
def third_vacancy():
    return Vacancies("Уборщик", "Убирать дом", "http://www.cleaner.ru", 50000, 0)


@pytest.fixture
def list_of_vacancies(one_vacancy, second_vacancy, third_vacancy):
    return [one_vacancy, second_vacancy, third_vacancy]
