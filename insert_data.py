import random
from faker import Faker
from pymongo import MongoClient
import uuid
import threading
from config import url
import time
import ssl

conn = MongoClient(url, ssl_cert_reqs=ssl.CERT_NONE)

def build_payload():
    user_id = str(uuid.uuid4())
    current_timestamp = time.time()

    page_change_payload = {
      "event": "pageStart",
      "properties": {
        "title": "Analytics Demo",
        "url": "https://brokercheck.finra.org/search/genericsearch/grid",
        "path": "/",
        "referrer": "https://brokercheck.finra.org/"
      },
      "user_id": user_id,
      "meta": {
        "timestamp": current_timestamp
      }
    }

    click_payload = {
      "event": "buttonClicked",
      "properties": {
        "foo": "bar",
        "lorem": "ipsum"
      },
      "options": {},
      "user_id": user_id,
      "meta": {
        "timestamp": current_timestamp
      }
    }

    return [page_change_payload, click_payload]


def main():
    for i in range(51):
        # arr of payloads:
        payloads_arr = build_payload()
        # all payloads
        for payload in payloads_arr:
            payload['inc'] = i
            p = conn.analytics.clickstream.insert_one(payload)
            print(f"user_id: {payload['user_id']} added for {payload['event']} \n inc: {i}")


if __name__ == '__main__':
    # delete collection
    # conn.analytics.clickstream.drop()
    # two threads
    for i in range(2):
        threading.Thread(target=main).start()
