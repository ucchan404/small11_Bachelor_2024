import handle_json_files as hjf

if __name__ == '__main__':
    data = hjf.load_json('raw_data.json', 'transactions-schema.json')
    for transaction in data['transactions']:
        print(transaction)
    hjf.write_to_json("new", data)
