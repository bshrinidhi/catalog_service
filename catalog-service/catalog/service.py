from catalog.utils.validation import *
from catalog.utils.util import getcollecteddata
from catalog.common.errors import BadRequest
from catalog.models.catalog import Catalog as C
import datetime
import uuid
from flask import jsonify
def create_catalog(catalog_data):
    validations = validate_create_catalog(catalog_data)
    if validations:
        raise BadRequest(validations)
    print(uuid.uuid4())
    catalog_data_json = catalog_data['catalog']
    print(catalog_data_json['ic_subset'])
    row=C.create( uid=uuid.uuid4(),created=datetime.datetime.now(),
                description=catalog_data_json['description'] if 'description' in catalog_data else '',
                ic_subset=catalog_data_json['ic_subset'] , name=catalog_data_json['name'],
                owner=catalog_data_json['owner'],
                status=catalog_data_json['status'] if 'status' in catalog_data else '',
                tags=catalog_data_json['tags'] if 'tags' in catalog_data else [],
                updated=datetime.datetime.now(),
                version=catalog_data_json['version'] if 'version' in catalog_data else '',
                visibility=catalog_data_json['visibility'])


    return row
def update_catalog(catalog_id,catalog_data):
    validations = validate_update_catalog(catalog_data)
    if validations:
        raise BadRequest(validations)
    catalog_data=catalog_data['catalog']
    row=C.objects.get(uid=catalog_id)
    collected=getcollecteddata(row)
    try:
        C.objects(uid=catalog_id).update(
            name=catalog_data['name'] if 'name' in catalog_data else collected['name'],
            description=catalog_data['description'] if 'description' in catalog_data else collected['description'],
            ic_subset__append=catalog_data['ic_subset'] if 'ic_subset' in catalog_data else [],
            owner=catalog_data['owner'] if 'owner' in catalog_data else collected['owner'],
            status=catalog_data['status'] if 'status' in catalog_data else collected['status'],
            updated=datetime.datetime.now(),
            tags__append=catalog_data['tags'] if 'tags' in catalog_data else [],
            version=catalog_data['version'] if 'version' in catalog_data else collected['version'],
            visibility=catalog_data['visibility'] if 'visibility' in catalog_data else collected['visibility']
        )
        response = jsonify({"message": "Updated successfully", "code": 200})
        return response
    except Exception as e:
        response = jsonify({"message": "hey there", "code": 500})
        response.status_code = 500
        return response



def delete_catalog(catalog_id):
    try:
        C.objects(uid=catalog_id).delete()
    except Exception as e:
        response = jsonify({"message": "Invalid catalog_id", "code": 500})
        response.status_code = 500
        return response

def get_catalogs():
    try:
        response=[]
        res=C.objects.all()
        for i in res:
            if i.visibility=="public":
                response.append((dict(i)))
        return jsonify(response)

    except Exception as e:
        print(e)
        return
