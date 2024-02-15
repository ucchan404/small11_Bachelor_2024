import handle_json_files as hjf


def remove_non_subscription_transactions(dataset, catalogue) -> list:
    new_dataset = []
    for item in dataset['transactions']:
        merchant = item['name']
        if merchant in catalogue:
            new_dataset.append(item)
        else:
            pass

    return new_dataset


def get_list_of_merchant(dataset) -> list:
    list_of_merchants_in_dataset = []
    for item in dataset:
        if item['name'] in list_of_merchants_in_dataset:
            pass
        else:
            list_of_merchants_in_dataset.append(item['name'])
    return list_of_merchants_in_dataset


def get_list_of_users(dataset) -> list:
    list_of_users_in_dataset = []
    for item in dataset:
        if item['userId'] in list_of_users_in_dataset:
            pass
        else:
            list_of_users_in_dataset.append(item['userId'])

    return list_of_users_in_dataset

def split_dataset(dataset):
    list_users = get_list_of_users(dataset)
    list_merchants = get_list_of_merchant(dataset)

    for merchant in list_merchants:
        new_list = []
        x = merchant
        for user in list_users:
            y = user
            for item in dataset:
                if item['name'] == x and item['userId'] == y:
                    new_list.append(item)
            hjf.write_to_json(f'user{y}_{x}', new_list)
