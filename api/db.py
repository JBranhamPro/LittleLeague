import pymongo
import properties as props

class MongoDB:
	"""docstring for MongoDB"""
	client = pymongo.MongoClient(props.Database.test_uri)
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