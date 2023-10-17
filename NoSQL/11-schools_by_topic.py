#!/usr/bin/env python3
""" returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school"""
    s_list = []
    for school in mongo_collection.find({'topics': topic}):
        s_list.append(school)
    return s_list
