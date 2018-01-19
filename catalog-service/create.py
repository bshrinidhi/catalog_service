from cassandra.cqlengine import columns
from catalog.models.base import BaseModel
from cassandra.cqlengine.management import sync_table
import uuid

class Catalog(BaseModel):
    name = columns.Text(required=True)
    description = columns.Text(required=False)
    ic_subset = columns.List(value_type=columns.Text, required=True)
    version = columns.Text(required=False)
    status = columns.Text(required=False)
    owner = columns.Text(required=True)
    visibility = columns.Text(required=True)
    tags = columns.List(value_type=columns.Text, required=False)
    ic_subset = columns.List(value_type=columns.Text, required=True)
sync_table(Catalog)