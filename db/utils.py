import json
from http import HTTPStatus


def build_response(err=None, res=None, status_code=HTTPStatus.OK, invoke_from_http=True):
    if invoke_from_http:
        response = {
            'statusCode': status_code,
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


