import uuid
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client["huaxia"]
students = db.students

# line 10-14 insert one student
student = {"first_name": "Byran", "last_name": "Wang", "grade": "10", "age": 13}

result = students.insert_one(student)
if result.acknowledged:
    print("One student Added. The student Id is", result.inserted_id)

# line 17-27 inssert many students
group1 = [
    {'_id':uuid.uuid4().hex,"first_name": "Arror", "last_name": "Yu", "grade": "10", "age": 14},
    {'_id':uuid.uuid4().hex,"first_name": "Joe", "last_name": "Johnson", "grade": "8", "age": 13},
    {'_id':uuid.uuid4().hex,"first_name": "Helen", "last_name": "Martin", "grade": "11", "age": 15},
    {'_id':uuid.uuid4().hex,"first_name": "Miky", "last_name": "Johnson", "grade": "7", "age": 12},
    {'_id':uuid.uuid4().hex,"first_name": "Macheal", "last_name": "Williams", "grade": "9", "age": 13}
]

results = students.insert_many(group1)
for id in results.inserted_ids:
   print("Student is Added. The Id is", str(id))

#students.delete_one({'_id':'4359008a994544cc87f379c4508637b7'})

#load all students in the database
allStudents = students.find()
for s in allStudents:
    pprint(s)

# studentAll = students.find({
#    'age':{
#        '$gt':11
#    }
# });
# for s in studentAll:
#    pprint(s)

#students = students.find().sort([('age', 1)])
#for s in students:
#    pprint(s)
#print(group1)

#classes = db.classes.find()
#for c in classes:
#    pprint(c)