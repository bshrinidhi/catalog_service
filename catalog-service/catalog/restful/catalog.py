from flask import jsonify, request
from flask_restful import Resource
from catalog.service import *
from catalog.common.errors import BadRequest


class Catalog(Resource):
    """
    Operations to list, edit and delete a single catalog
    """
    def get(self, catalog_id):
        """Return a single catalog"""
        return "test"

    def put(self, catalog_id):
        """Edit a single catalog"""
        try:
            if not request.data:
                raise BadRequest("CATALOG_ATTRS_MISSING")
            response=update_catalog(catalog_id,request.get_json())
            return response
        except BadRequest as be:
            response = jsonify(be.response)
            response.status_code = 400
            return response
        except Exception as e:
            response = jsonify({"message": "hey there exception", "code":500})
            response.status_code = 500
            return response


    def delete(self, catalog_id):
        """Delete a single catalog"""
        try:
            if not request.data:
                raise BadRequest("CATALOG_ATTRS_MISSING")
            delete_catalog(catalog_id)
            response = jsonify({"message": "Successfully deleted", "code": 200})
            return response
        except BadRequest as be:
            response = jsonify(be.response)
            response.status_code = 400
            return response
        except Exception as e:
            response = jsonify({"message": "catalog_id not found", "code":500})
            response.status_code = 500
            return response

