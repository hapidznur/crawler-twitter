from pymongo import MongoClient
import pprint
import logging
client = MongoClient()
client = MongoClient('localhost', 27017)
DATABASE = 'PUSTU'
db =  client.DATABASE

class MongoModel():
    def __init__(self):
        pass

    def mongo_add(self, _data, _collection):
        try:
            tweets = db['%s' % _collection]  
            post_id = tweets.insert_one(_data).inserted_id
        
        except ValueError:
            print(ValueError)

    def mongo_insert_replies(self, _data, _collection):
        try:
            tweets = db['%s' % _collection]  
            post_id = tweets.insert_one(_data).inserted_id
        
        except ValueError:
            print(ValueError)

    def mongo_twitter(self, _limit = 10, _collection =  None):
        try:
            tweets = db['%s' % _collection]  
            data = tweets.find().limit(_limit)
        except ValueError:
            logging.error(ValueError)

        return data

    def mongo_replies(self, _limit = 10, _collection =  None):
        try:
            tweets = db['%s' % _collection]  
            data = tweets.find().limit(_limit)
        except ValueError:
            logging.error(ValueError)

        return data

if __name__ == '__main__':
    ex = MongoModel()
    test = {'test1': 'test'}
    ex.mongo_insert_replies(test, 'test1')
    ex.mongo_insert_replies(test, 'test2')
 


# from pyArango.connection import *
# conn = Connection(username="root", password="RANDOM")
# b = conn.createDatabase(name="twitter")
# db = conn["school"]
# studentsCollection = db.createCollection(name="Students")
# doc1 = studentsCollection.createDocument()
# def update_gpa(key, new_gpa):
#     doc = studentsCollection[key]
#     doc['gpa'] = new_gpa
#     doc.save()
# def top_scores(col, gpa):
#     print("Top Soring Students:")
#     for student in col.fetchAll():
#         if student['gpa'] >= gpa:
#             print("- %s" % student['name'])
