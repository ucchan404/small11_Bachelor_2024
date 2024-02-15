from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json


def load_json(datafile, schemafile) -> list:
    with open('Data/' + datafile) as f:
        data = json.load(f)

    with open(schemafile) as f:
        schema = json.load(f)

    try:
        validate(instance=data, schema=schema)
        print("Validation successful!")
    except ValidationError as e:
        print("Validation failed!")
        print(f"Error message: {e.message} in {e.json_path}")

    return data


def load_json_without_schema(filename) -> list:
    with open('Data/' + filename) as f:
        data = json.load(f)
    return data


def write_to_json(filename, dataset):
    with open("Data/" + filename + ".json", "w") as f:
        json.dump(dataset, f, indent=2)
