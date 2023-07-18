import json
from src.Operation import Operation


def load_json(file_path: str) -> list:
    """
    Deserializing a json object
    :param file_path: the path to the file
    :return: dictionary with data from json
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)


def get_list_with_executed_operations(raw_list: list) -> list:
    """
    Getting the list of executed operations
    :param raw_list: list of operations
    :return: list of executed operations
    """
    list_with_executed_operations = []

    for item in raw_list:

        # Checking for an empty element
        if item == {}:
            continue

        # Getting the data from the json
        date = item['date']
        description = item['description']
        try:
            sender = item['from']
        except KeyError:
            sender = None
        operation_id = int(item["id"])
        amount = float(item["operationAmount"]['amount'])
        currency_code = item["operationAmount"]['currency']["code"]
        currency_name = item["operationAmount"]['currency']["name"]
        state = item['state']
        destination = item['to']

        # Building the object
        item = Operation(operation_id,
                         state,
                         date,
                         amount,
                         currency_name,
                         currency_code,
                         description,
                         destination,
                         sender
                         )
        # Adding the object to the list
        if item.state == "EXECUTED":
            list_with_executed_operations.append(item)

    return list_with_executed_operations


def sort_list_by_date(list_with_executed_operations: list) -> list:
    """
    Sorting the list of executed operations by date
    :param list_with_executed_operations: list of executed operations
    :return: sorted list of executed operations
    """
    list_with_executed_operations.sort(key=lambda x: x.date, reverse=True)

    return list_with_executed_operations
