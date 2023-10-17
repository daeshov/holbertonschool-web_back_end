#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient

def get_nginx_logs_stats():
    """_summary_Connect to the MongoDB server."""
    client = MongoClient('mongodb://localhost:27017')

    # Access the logs database and the nginx collection
    db = client.logs
    collection = db.nginx

    # Count the total number of logs
    total_logs = collection.count_documents({})

    # Count logs by HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}

    # Count logs with method=GET and path=/status
    special_log_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print the statistics
    print(f"{total_logs} logs where x is the number of documents in this collection")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\t{method}: {count} logs")
    print(f"method=GET\npath=/status: {special_log_count} logs")

if __name__ == "__main__":
    get_nginx_logs_stats()
