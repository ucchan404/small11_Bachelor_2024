from datetime import datetime, date
from typing import Optional, List
from dataclasses_json import Undefined, dataclass_json, config
from dataclasses import dataclass, field, asdict
from marshmallow import fields
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Transaction:
    id: int
    amount: float
    name: str
    userId: int
    transactionDate: date = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.Date(format='iso')
        )
    )


@dataclass_json(undefined=Undefined.EXCLUDE)  # Ignore unknown fields in output
@dataclass
class Dataset:
    transactions: List[Transaction]

    def __post_init__(self):  # Forces the use of custom dataclass
        self.transactions = [Transaction(**transaction) for transaction in self.transactions]
    def toJson(self):
        return json.dumps(asdict(self))

def load_json(datafile, schemafile):
    with open('Data/' + datafile) as f:
        data = json.load(f)

    with open(schemafile) as f:
        schema = json.load(f)

    try:
        validate(instance=data, schema=schema)
        print("Validation successful!")
    except ValidationError as e:
        print("Validation failed!")
        print(f"Error message: {e.message}")

    raw_trans = Dataset(data)
    print(raw_trans.transactions[:1])
def write_to_json(filename, dataset):
    with open(filename + ".json", "w") as newJsonFile:
        newJsonFile.write(dataset.toJson())

if __name__ == '__main__':
    load_json('raw_data.json', 'transactions-schema.json')
