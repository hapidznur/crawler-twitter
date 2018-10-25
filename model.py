from pymongo import MongoClient
import pprint
import logging
client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.pustu
def mongo_add(_data):
    try:
        tweets = db.pustu
        post_id = tweets.insert_one(_data).inserted_id
    except ValueError:
        print(ValueError)

def mongo_read(_limit=10):
    try:
        tweets =  db.pustu
        data = tweets.find().limit(_limit)
    except ValueError:
        logging.error(ValueError)

    return data
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