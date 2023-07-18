from src.utils import load_json, sort_list_by_date, get_list_with_executed_operations


def test_load_json(data_for_load_json):
    path, expected = data_for_load_json
    assert load_json(path) == expected


def test_get_list_with_executed_operations(data_for_get_list_with_executed_operations):
    test_list, expected_list = data_for_get_list_with_executed_operations
    test_list = get_list_with_executed_operations(test_list)

    assert expected_list[0].operation_id == test_list[0].operation_id
    assert expected_list[1].operation_id == test_list[1].operation_id


def test_sort_list_by_date(data_for_sort_list_by_date):
    test_list, expected_list = data_for_sort_list_by_date
    test_list = sort_list_by_date(test_list)

    assert expected_list[0].operation_id == test_list[0].operation_id
    assert expected_list[1].operation_id == test_list[1].operation_id
