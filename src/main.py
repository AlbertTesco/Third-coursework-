from src.utils import *
import os.path

if __name__ == '__main__':
    # load data from json
    list_from_json = load_json(os.path.join("../data", "operations.json"))
    # get list with executed operations
    list_from_json = get_list_with_executed_operations(list_from_json)
    # sort list by date
    list_from_json = sort_list_by_date(list_from_json)
    # print first 6 operations
    for operation in list_from_json[0:5]:
        print(operation.get_operation_info())
