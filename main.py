import json

import handle_json_files as hjf
import analyse_data as ad
import clean_data as cd

if __name__ == '__main__':
    data = hjf.load_json('raw_data.json', 'transactions-schema.json')

    catalogue = hjf.load_json_without_schema('merchants_catalogue.json')
    raw_data = hjf.load_json_without_schema('raw_data.json')
    cd.remove_missing_data(raw_data)
    clean_data = hjf.load_json('clean_data.json', 'transactions-schema.json')
    new_data = ad.remove_non_subscription_transactions(clean_data, catalogue)
    ad.split_dataset(new_data)




