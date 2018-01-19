from flask import jsonify, request
from flask_restful import Resource
from catalog.service import *
from catalog.common.errors import BadRequest


class Catalogs(Resource):
    """
    Operations to list all catalogs and create new catalogs
    """
    def get(self):
        """Return a list of all the catalogs"""
        try:
            response=get_catalogs()
            return response
        except BadRequest as be:
            response = jsonify(be.response)
            response.status_code = 400
            return response
        except Exception as e:
            response = jsonify({"message": "hey there exception", "code":500})
            response.status_code = 500
            return response

    def post(self):
        """Create a new catalog"""
        try:
            if not request.data:
                raise BadRequest("CATALOG_ATTRS_MISSING")
            create_catalog(request.get_json())
            response = jsonify({"message": "Successfully Inserted", "code": 200})
            return response
        except BadRequest as be:
            response = jsonify(be.response)
            response.status_code = 400
            return response
        except Exception as e:
            response = jsonify({"message": "hey there", "code":500})
            response.status_code = 500
            return response
