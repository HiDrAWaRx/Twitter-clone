from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    if isinstance(exc, DatabaseError):
        error_response = {
            'ErrorDetail': 'Ocurrió un error en la base de datos.'
        }
        return Response(error_response, status=500)
    
    return exception_handler(exc, context)