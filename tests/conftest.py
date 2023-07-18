import json
import pytest
from src.Operation import Operation
from src.utils import get_list_with_executed_operations


# Data for test utils.py
@pytest.fixture(scope="session")
def data_for_load_json():
    path = 'test.json'
    with open(path, 'r') as f:
        expected = json.load(f)
    return path, expected


@pytest.fixture(scope="session")
def data_for_get_list_with_executed_operations():
    path = 'test.json'
    with open(path, 'r') as f:
        tested = json.load(f)
    expected = [
        Operation(operation_id=716496732, state="EXECUTED", date="2018-04-04T17:33:34.701093", amount=40701.91,
                  currency_name="USD", currency_code="USD",
                  description="Перевод организации",
                  destination="Счет 72731966109147704472", sender="Visa Gold 5999414228426353"),
        Operation(operation_id=441945886, state="EXECUTED", date="2019-08-26T10:50:58.294041", amount=31957.58,
                  currency_name="руб.", currency_code="RUB",
                  description="Перевод организации", destination="Счет 64686473678894779589",
                  sender="Maestro 1596837868705199")
    ]

    return tested, expected


@pytest.fixture(scope="session")
def data_for_sort_list_by_date():
    path = 'test.json'
    with open(path, 'r') as f:
        tested = json.load(f)
    tested = get_list_with_executed_operations(tested)

    expected = [
        Operation(operation_id=441945886, state="EXECUTED", date="2019-08-26T10:50:58.294041", amount=31957.58,
                  currency_name="руб.", currency_code="RUB",
                  description="Перевод организации", destination="Счет 64686473678894779589",
                  sender="Maestro 1596837868705199"),
        Operation(operation_id=716496732, state="EXECUTED", date="2018-04-04T17:33:34.701093", amount=40701.91,
                  currency_name="USD", currency_code="USD",
                  description="Перевод организации",
                  destination="Счет 72731966109147704472", sender="Visa Gold 5999414228426353")
    ]

    return tested, expected


# Data for test utils.py
@pytest.fixture(scope="session")
def data_for_get_masked_sender_info():
    return [
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 27248529432547658655", "Счет 2724 85** **** 4765 8655")
    ]


@pytest.fixture(scope="session")
def data_for_get_masked_destination_info():
    return [
        ("Счет 96291777776753236930", "Счет **6930"),
        ("Счет 89685546118890842412", "Счет **2412"),
        ("Maestro 3806652527413662", "Maestro **3662")
    ]


@pytest.fixture(scope="session")
def data_for_test_get_data():
    return [
        ("2018-03-02T02:03:11.563721", "02.03.2018"),
        ("2018-12-28T23:10:35.459698", "28.12.2018"),
        ("2019-09-29T14:25:28.588059", "29.09.2019"),
    ]


@pytest.fixture(scope="session")
def data_for_get_operation_info():
    return ["26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n",
            "04.04.2018 Перевод организации\nСчет **4472\n40701.91 USD\n"]
