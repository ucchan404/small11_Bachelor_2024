import json

import handle_json_files as hjf
import analyse_data as ad
import clean_data as cd

if __name__ == '__main__':
    data = hjf.load_json('raw_data.json', 'transactions-schema.json')

    cd.clean_data('raw_data.json')
    new_data = hjf.load_json('clean_data.json', 'transactions-schema.json')

    ad.split_dataset(new_data)

    # missing_date = hjf.load_json_without_schema('user1_Netflix.json')
    # ad.replace_missing_date(missing_date)


