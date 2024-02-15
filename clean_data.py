import handle_json_files as hjf
import transactions


def remove_missing_data(dataset):
    new_dataset = []
    for item in dataset['transactions']:
        if item['name'] == "" or item['amount'] == "" or item['userId'] == "":
            pass

        else:
            if item not in new_dataset:
                new_dataset.append(item)

    new_dict = {"transactions": new_dataset}
    hjf.write_to_json("clean_data", new_dict)
