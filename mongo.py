import pymongo 
import datetime

client = pymongo.MongoClient("mongodb+srv://ArdikaPurna:dikadika@cluster0.nlbrpup.mongodb.net/?retryWrites=true&w=majority")
db = client.test
my_collections = db.Koleksi

def save_data(kecepatan,latitude,longitude):
    try:
        data = {

            "kecepatan": kecepatan,
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": datetime.datetime.now()
        }

        hasil = my_collections.insert_one(data)

        print("Data inserted", hasil)
        return True, None
    except Exception as e:
        return False, str(e)
        