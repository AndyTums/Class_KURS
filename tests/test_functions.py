from src.functions import top_vacancies, filter_words, sorting_of_salary, work_with_user


def test_top_vacancies(list_of_vacancies):
    assert len(top_vacancies(list_of_vacancies, 1)) == 1


def test_filter_words(list_of_vacancies):
    assert len(filter_words(list_of_vacancies, "ГОТОВИТЬ")) == 1


def test_sorting_of_salary(list_of_vacancies):
    assert len(sorting_of_salary(list_of_vacancies, 0, 100000)) == 3
    assert len(sorting_of_salary(list_of_vacancies, 0, 50000)) == 2
    assert len(sorting_of_salary(list_of_vacancies, 90000, 100000)) == 0


def test_work_with_user(capsys, third_vacancy):
    work_with_user([third_vacancy])

    captured = capsys.readouterr()

    expected_output = ('Название вакансии: Уборщик\n'
                       'Описание: Убирать дом\n'
                       'Ссылка на вакансию: http://www.cleaner.ru\n'
                       'Зарплата: 50000\n'
                       '\n').strip()

    # Проверка соответствия захваченного вывода и ожидаемого результата
    assert captured.out.strip() == expected_output
