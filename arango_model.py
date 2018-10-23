from pyArango.connection import *
conn = Connection(username="root", password="RANDOM")

b = conn.createDatabase(name="twitter")
db = conn["school"]

studentsCollection = db.createCollection(name="Students")

doc1 = studentsCollection.createDocument()

def update_gpa(key, new_gpa):
    doc = studentsCollection[key]
    doc['gpa'] = new_gpa
    doc.save()

def top_scores(col, gpa):
    print("Top Soring Students:")
    for student in col.fetchAll():
        if student['gpa'] >= gpa:
            print("- %s" % student['name'])