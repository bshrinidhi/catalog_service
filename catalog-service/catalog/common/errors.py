from flask_restful import HTTPException
from catalog.common.constants import *


class BadRequest(HTTPException):
    def __init__(self, error_code):
        if type(error_code) == str:
            self.response = {
                "message": eval(error_code),
                "recommended": eval(error_code+'_REC'),
                "code": error_code
            }
        elif type(error_code) == list:
            self.response = []
            for error in error_code:
                self.response.append({
                    "message": eval(error),
                    "recommended": eval(error+'_REC'),
                    "code": error
                })


class ResourceNotFound(HTTPException):
    code = 404


custom_errors = {
    'BadRequest': {
        'message': 'Invalid Input',
        'code': "INVALID_INPUT",
        'recommended': 'recommended action'
    },
    'ResourceNotFound': {
        'message': 'Resource Not Found',
        'status': 404
    }
}