from datetime import datetime
import ssl
from config import datalake_url
from pymongo import MongoClient

conn = MongoClient(datalake_url, ssl_cert_reqs=ssl.CERT_NONE)

split_inc = 25

pipeline = [
    {
        '$match': {
            'inc': {
                '$lt': split_inc
            }
        }
    },
    {
        '$out': {
            's3': {
                'bucket': 'esteininger-personal-datalake',
                'filename': 'test',
                "region": "us-east-2",
                'format': {
                    'name': 'json'
                }
            }
        }
    }
]

c = conn['esteininger-personal-datalake'].clickstream.aggregate(pipeline)
print(list(c))
print('Archive created!')
