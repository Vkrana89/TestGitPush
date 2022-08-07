import pymongo

client = pymongo.MongoClient("mongodb+srv://vkranavivek:Blackpearl1*@cluster0035819.2aoyu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "vivek",
    "email": "rvivek@moog.com",
    "surname" : "rana"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)