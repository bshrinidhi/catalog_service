from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
import uuid,datetime
class BaseModel(Model):
    uid = columns.UUID(primary_key=True, default=uuid.uuid4)
    created = columns.DateTime(required=True, default=columns.datetime.now)
    updated = columns.DateTime(required=True, default=columns.datetime.now)
