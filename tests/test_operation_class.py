from src.Operation import *
from src.utils import sort_list_by_date, get_list_with_executed_operations, load_json


def test_get_masked_sender_info(data_for_get_masked_sender_info):
    for tested, expected in data_for_get_masked_sender_info:
        instance = Operation(1, "Test", "Test", 1, "Test", "Test", "Test", "Test", tested)
        assert instance.get_masked_sender_info() == expected


def test_get_masked_destination_info(data_for_get_masked_destination_info):
    for tested, expected in data_for_get_masked_destination_info:
        instance = Operation(1, "Test", "Test", 1, "Test", "Test", "Test", tested, "Test")
        assert instance.get_masked_destination_info() == expected


def test_get_data(data_for_test_get_data):
    for tested, expected in data_for_test_get_data:
        instance = Operation(1, "Test", tested, 1, "Test", "Test", "Test", "Test", "Test")
        assert instance.get_data() == expected


def test_get_operation_info(data_for_get_operation_info):
    expected = data_for_get_operation_info

    file = load_json('test.json')

    file = get_list_with_executed_operations(file)
    file = sort_list_by_date(file)

    index = 0
    for item in file:
        assert item.get_operation_info() == str(expected[index])
        index += 1
