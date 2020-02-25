import json
from http import HTTPStatus


def bad_request(errors=None, invoke_from_http=True):
    message = {'message': 'Bad request'} if not errors else errors
    return build_response(err=message,
                          status_code=HTTPStatus.BAD_REQUEST,
                          invoke_from_http=invoke_from_http)


def build_response(err=None, res=None, status_code=HTTPStatus.OK, invoke_from_http=True):
    if invoke_from_http:
        response = {
            'status_code': status_code,
            'body': json.dumps(err) if err else json.dumps(res),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    else:
        response = {
            'statusCode': status_code,
            'body': err if err else res
        }
    return response


def ok(data, invoke_from_http=True):
    return build_response(res=data, status_code=HTTPStatus.OK,
                          invoke_from_http=invoke_from_http)


