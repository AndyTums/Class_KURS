from src.work_with_vacancies import Vacancies


def test_vacancies(one_vacancy):
    assert one_vacancy.name == "Курьер"
    assert one_vacancy.description == "Доставка товара"
    assert one_vacancy.url == "http://www.search.ru"
    assert one_vacancy.salary_from == 30000
    assert one_vacancy.salary_to == 50000


def test_cast_to_object_class(info_api):
    vacans = Vacancies.cast_to_object_list(info_api)
    assert len(vacans) == 1
    assert vacans[0].name == "Курьер - Сборщик"
    assert vacans[0].description == ("Доставлять - собирать заказы от интернет-магазинов. "
                                     "Использовать мобильное приложение для получения заказов и "
                                     "информации о маршруте или составе заказа.")
    assert vacans[0].url == "https://api.hh.ru/areas/47"
    assert vacans[0].salary_from == 10000
    assert vacans[0].salary_to == 50000


def test_lt_(one_vacancy, second_vacancy):
    assert Vacancies.__lt__(one_vacancy, second_vacancy) is False
    assert Vacancies.__lt__(second_vacancy, one_vacancy) is True
