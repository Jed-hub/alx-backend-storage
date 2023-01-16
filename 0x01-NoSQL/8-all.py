#!/usr/bin/env python3
""" all module """
import pymongo


def list_all(mongo_collection):
    x = mongo_collection.find()
    return x
