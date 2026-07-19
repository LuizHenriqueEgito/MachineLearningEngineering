from pathlib import Path
from datetime import timedelta

import polars as pl

from feast import (
    Entity,
    FeatureView,
    Field,
    FileSource,
)

from feast.types import Float64
from feast.value_type import ValueType


TRAIN_FILE = Path(
    "../00_dataset/02_final_data/df_train.pq"
)

transaction = Entity(
    name="transaction",
    join_keys=["transaction_id"],
    value_type=ValueType.INT64,
)

source = FileSource(
    path=str(TRAIN_FILE.resolve()),
    timestamp_field="transaction_time",
)


schema = pl.read_parquet_schema(TRAIN_FILE)

ignore = {
    "transaction_id",
    "transaction_time",
    "label",
}


fields = []

for name, dtype in schema.items():
    if name in ignore:
        continue
    fields.append(
        Field(
            name=name,
            dtype=Float64
        )
    )

print("Features criadas:")
print([f.name for f in fields])


transaction_features = FeatureView(
    name="transaction_features",
    entities=[transaction],
    ttl=timedelta(days=3650),
    schema=fields,
    source=source,
    online=True,
)