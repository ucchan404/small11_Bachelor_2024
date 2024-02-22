import json

import handle_json_files as hjf
import pandas as pd
import numpy as np


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
    for item in dataset['transactions']:
        if item['name'] in list_of_merchants_in_dataset:
            pass
        else:
            list_of_merchants_in_dataset.append(item['name'])
    return list_of_merchants_in_dataset


def get_list_of_users(dataset) -> list:
    list_of_users_in_dataset = []
    for item in dataset['transactions']:
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
            for item in dataset['transactions']:

                if item['name'] == x and item['userId'] == y:
                    new_list.append(item)
            hjf.write_to_json(f'user{y}_{x}', new_list)


def replace_missing_date(dataset):
    for item in dataset:
        transaction_id = item['id']
        if item['transactionDate'] == "":
            df = pd.DataFrame(columns=['date', 'id'])
            frequency = find_payment_frequency(df, dataset)

            if frequency.size > 1:
                print('Multiple payment frequencies')
            else:
                start = df['date'][0].date()
                end = df['date'][len(df) - 1].date()
                if frequency.item() < 30:
                    df['new_dates'] = pd.date_range(start=start, end=end, freq=f'{frequency.item()}D')
                    df['new_dates'] = df['new_dates'].dt.strftime('%d-%m-%Y')
                    date = df.loc[df.id == transaction_id, 'new_dates'].values[0]

                    item['transactionDate'] = date
                if 30 <= frequency.item() <= 31:
                    df['new_dates'] = pd.date_range(start=start, end=end, freq='MS')
                    df['new_dates'] = df['new_dates'].dt.strftime('%d-%m-%Y')
                    date = df.loc[df.id == transaction_id, 'new_dates'].values[0]

                    item['transactionDate'] = date

            print(json.dumps(dataset, indent=2))


def find_payment_frequency(df: pd.DataFrame, dataset) -> str:
    for date in dataset:
        new_row = {'date': date['transactionDate'],
                   'id': date['id']}
        df.loc[len(df)] = new_row
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df = df.sort_values(by='id')
    df['diff'] = df['date'].diff()
    frequency = df['diff'].mode(dropna=True)
    x = frequency.dt.days
    return x
