from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client['test-database']
courses = db.courses

bryan = {
    'Instructor':'Bryan Wang',
    'course':'Java Tutorial',
    'price':100,
    'rating':5
} 

#Create
# result = courses.insert_one(bryan)
# if result.acknowledged:q
#    print("Course Added. The course Id is", result.inserted_id)

#Read
#john = courses.find_one({'Instructor':'John Wang'})
john = courses.find_one({'_id':ObjectId('5ea0ae29bc90718b663ab9c7')})
print(john)

#Update
new_price = {"price":150,"course":"Game"}
result = courses.update_one(
    {'_id':ObjectId('5ea0ae29bc90718b663ab9c7')},
    {'$set':new_price}
)


#Delete
x = courses.delete_one({'_id':ObjectId('5ea0b0fde402aba68dfe8919')})
print(x.deleted_count)