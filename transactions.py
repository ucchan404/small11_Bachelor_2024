from datetime import datetime, date
from typing import Optional, List
from dataclasses_json import Undefined, dataclass_json, config
from dataclasses import dataclass, field, asdict
from marshmallow import fields

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





