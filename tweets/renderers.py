from rest_framework import renderers
import json

class DefaultRenderer(renderers.JSONRenderer):
    charset='utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):

        if 'ErrorDetail' in str(data):
            error_message = None

            for field, errors in data.items():
                if errors:
                    error_message = f"{field}: {errors[0]}"
                    break
            success = False
            error_code = data if 'error_code' in str(data) else None
            message = error_message
            response_data = {'error': data}
        else:
            success = True
            error_code = 0
            message = "Everything ok"
            response_data = data

        return json.dumps({
            "success": success,
            "message": message,
            "error_code": error_code,
            "data": response_data
        })