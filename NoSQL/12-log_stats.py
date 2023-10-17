#!/usr/bin/env python3
"This is a line of text"
from pymongo import MongoClient


if __name__ == "__main__":
    "This is a line of text"
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    print(f"{nginx_collection.count_documents({})} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {nginx_collection.count_documents({'method': method})}")

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
    