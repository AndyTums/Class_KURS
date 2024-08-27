import pytest
from unittest.mock import Mock, patch

from src.work_with_API import HeadHunter

# @patch("requests.get")
# def test_get_info(mock):
#     head = HeadHunter()
#     mock.return_value.status_code = 200
#     mock.return_value = {'items': [
#         {'id': '46356776', 'premium': False, 'name': 'Продавец натуральных сладостей (еженедельная оплата)',
#          'department': None, 'has_test': False, 'response_letter_required': False,
#          'area': {'id': '53', 'name': 'Краснодар', 'url': 'https://api.hh.ru/areas/53'},
#          'salary': {'from': 48000, 'to': 92000, 'currency': 'RUR', 'gross': False},
#          'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
#          'published_at': '2024-08-09T21:48:12+0300', 'created_at': '2024-08-09T21:48:12+0300', 'archived': False,
#          'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=46356776',
#          'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/46356776?host=hh.ru',
#          'alternate_url': 'https://hh.ru/vacancy/46356776', 'relations': [],
#          'employer': {'id': '5576898', 'name': 'Галактионов Кирилл Анатольевич',
#                       'url': 'https://api.hh.ru/employers/5576898', 'alternate_url': 'https://hh.ru/employer/5576898',
#                       'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5576898',
#                       'accredited_it_employer': False, 'trusted': True},
#          'snippet': {'requirement': 'Готовность к обучению. Желание зарабатывать. Активная жизненная позиция.',
#                      'responsibility': 'Открытие/закрытие торгового филиала. Консультация по ассортименту продукции. Работа с кассой. Продажи.'},
#          'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
#          'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
#          'professional_roles': [{'id': '97', 'name': 'Продавец-консультант, продавец-кассир'}],
#          'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
#          'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
#          'adv_context': None}]}
#     assert head.get_info() == [
#         {'id': '46356776', 'premium': False, 'name': 'Продавец натуральных сладостей (еженедельная оплата)',
#          'department': None, 'has_test': False, 'response_letter_required': False,
#          'area': {'id': '53', 'name': 'Краснодар', 'url': 'https://api.hh.ru/areas/53'},
#          'salary': {'from': 48000, 'to': 92000, 'currency': 'RUR', 'gross': False},
#          'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
#          'published_at': '2024-08-09T21:48:12+0300', 'created_at': '2024-08-09T21:48:12+0300', 'archived': False,
#          'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=46356776',
#          'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/46356776?host=hh.ru',
#          'alternate_url': 'https://hh.ru/vacancy/46356776', 'relations': [],
#          'employer': {'id': '5576898', 'name': 'Галактионов Кирилл Анатольевич',
#                       'url': 'https://api.hh.ru/employers/5576898', 'alternate_url': 'https://hh.ru/employer/5576898',
#                       'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5576898',
#                       'accredited_it_employer': False, 'trusted': True},
#          'snippet': {'requirement': 'Готовность к обучению. Желание зарабатывать. Активная жизненная позиция.',
#                      'responsibility': 'Открытие/закрытие торгового филиала. Консультация по ассортименту продукции. Работа с кассой. Продажи.'},
#          'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
#          'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
#          'professional_roles': [{'id': '97', 'name': 'Продавец-консультант, продавец-кассир'}],
#          'accept_incomplete_resumes': True, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
#          'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
#          'adv_context': None}]
