from datetime import datetime
import ssl
from config import datalake_url
from pymongo import MongoClient
from pprint import pprint

conn = MongoClient(datalake_url, ssl_cert_reqs=ssl.CERT_NONE)['esteininger-personal-datalake']

# 1st: create schema
# c = conn.command({'sqlGenerateSchema': 1})
# pprint(c)


# 2nd: show that schema was created
# sql = 'select TABLE_NAME from INFORMATION_SCHEMA.TABLES'
# pipeline = [
#     {
#         '$sql': {
#             'statement': sql,
#             'format': "jdbc",
#             'dialect': "mysql",
#         }
#     }
# ]
#
# r = conn.aggregate(pipeline)
# pprint(list(r))

# 3rd: query mongodb cluster
# sql = "select * from `analytics.1` limit 2"
#
# pipeline = [
#     {
#         '$sql': {
#             'statement': sql,
#             'format': "jdbc",
#             'dialect': "mysql",
#         }
#     }
# ]
#
# r = conn.aggregate(pipeline)
# pprint(list(r))

# 4th: query S3 via atlas data lake
sql = "select * from `clickstream` limit 2"

pipeline = [
    {
        '$sql': {
            'statement': sql,
            'format': "jdbc",
            'dialect': "mysql",
        }
    }
]

r = conn.aggregate(pipeline)
pprint(list(r))
