import logging

import pymongo

from api.app import config

LOGGER = logging.getLogger('ll_db_log')


class InMemDB(object):
    """docstring for InMemDB"""
    def __init__(self, arg):
        super(InMemDB, self).__init__()
        self.games = {}
        self.users = {}

    # TODO: Need to add validation to this method when we move to a real database
    # insert new user into the Little League database
    # Returns True if the user was added or already in the database
    # Returns False if they could not be added
    def insert_object(self, object_details):
        object_id = object_details['object_id']

        if object_type == 'game':
            object_store = self.games
        elif object_type == 'user':
            object_store = self.users
        
        if self.object_store.get(object_id):
            LOGGER.warn(f"The object with the ID, {object_id}, is already present in the database.")
            updated = self.update_object(object_details)
            return updated

        self.object_store[object_id] = object_details
        return True

    def update_object(self, object_details):
        object_id = object_details['_id']
        object_type = object_details['_type']
        
        if object_type == 'game':
            object_store = self.games
        elif object_type == 'user':
            object_store = self.users
            
        old_object = self.object_store[object_id]
        updated_object = {}
        
        for detail in list(old_object.keys()):
            updated_object[detail] = object_details.get(detail, old_object[detail])

        self.object_store[object_id] = updated_object
        return updated_object


class MongoDB:
    """docstring for MongoDB"""
    client = pymongo.MongoClient(config.Database.test_uri)
    db = client.test

    def insert_user(self, user_details):
        collection = db.users
        _id = user_details.get('id')
        display_name = user_details.get('display_name')
        doc = {}

        if _id:
            verify_id(_id)
            collection.insert_one({'_id': _id})

    def verify_user_id(_id):
        collection = db.users
        matches = collection.find({'_id'})
