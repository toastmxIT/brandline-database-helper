import sys
import os
import json
import psycopg2
from psycopg2 import OperationalError
from psycopg2.extras import RealDictCursor
from cerberus import Validator
from schemas import RUN_QUERY_SCHEMA
from utils import ok

rds_host = os.getenv('RDS_HOST')
name = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')

RUN_QUERY_VALIDATOR = Validator(RUN_QUERY_SCHEMA)


def lambda_handler(event, context):
    action = event['action']
    if action == 'run':
        if RUN_QUERY_VALIDATOR.validate(event):
            queries = event['queries']
            response = execute_queries(queries)
            return response
        else:
            return 'Not Hello World!'


def execute_queries(queries):
    """
    This function fetches content from MySQL RDS instance
    """
    conn = dbconnect()

    result = []

    for query in queries:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            try:
                cur.execute(query)
                rows = cur.fetchall()
                result.append(json.dumps(rows, indent=2))
            except Exception as e:
                print(e)
    return ok(result)

def dbconnect():
    try:
        return psycopg2.connect(host=rds_host, user=name, password=password, dbname=db_name, port=port)
    except OperationalError as e:
        # err_type, err_obj, traceback = sys.exc_info()
        # return err_type
        sys.exit()
