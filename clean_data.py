import json
import string

import handle_json_files as hjf
import transactions


def remove_missing_data(dataset) -> dict:
    new_dataset = []
    for item in dataset['transactions']:
        if item['name'] == "" or item['amount'] == "" or item['userId'] == "":
            pass

        else:
            if item not in new_dataset:
                new_dataset.append(item)
    new_dict = {"transactions": new_dataset}
    return new_dict


def change_amount_to_number(dataset) -> list:
    for item in dataset['transactions']:
        if type(item['amount']) == int:
            x = item['amount']
            y = float(x)
            item['amount'] = y
        if type(item['amount']) == str:
            x = item['amount'].replace(",", ".")
            y = float(x)
            item['amount'] = y

    return dataset


def clean_data(filename):
    raw_data = hjf.load_json_without_schema(filename)
    new_data = remove_missing_data(raw_data)
    new_data = change_amount_to_number(new_data)
    hjf.write_to_json("clean_data", new_data)
