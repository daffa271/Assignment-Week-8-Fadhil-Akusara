import pymongo
import datetime


client = pymongo.MongoClient("mongodb+srv://Fadhil19:Fadhil12345@cluster0.gkpze5c.mongodb.net/?retryWrites=true&w=majority")
db = client.SICFadhil
my_collections = db.AssWeek8

speed1 = {
    "kecepatan": 90,
    "latitude": 6.2088,
    "longitude": 106.8456
}
speed2 = {
    "kecpatan": 60,
    "latitude": -6.193125,
    "longitude": 106.821810
}

results = my_collections.insert_many([speed1,speed2])
print(results.inserted_ids)