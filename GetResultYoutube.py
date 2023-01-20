
import requests
import time
from pymongo import MongoClient
def get_database():
 
   CONNECTION_STRING = "mongodb+srv://test:test@cluster0.a0aucfd.mongodb.net/?retryWrites=true&w=majority"
 
   client = MongoClient(CONNECTION_STRING)
 
   return client['YoutubeData']

def get_responses(query):
    collection = dbname[query]
    print(query)
    link = "https://youtube.googleapis.com/youtube/v3/search?order=date&key=AIzaSyDd-OUNS3ywymBwfPv4FHcfWJHNomKLMPU&part=snippet&q="+query

    response = requests.get(link)

    response = response.json()

    index = 1
    if "items" in response:

        for item in response["items"]:
            # print(item , index)
            
            collection.update_one({"_id":index}, {
                "$set": {
                "title":item["snippet"]["title"],
                "publishedAt":item["snippet"]["publishedAt"],
                "description":item["snippet"]["description"],
                "thumbnails" : item["snippet"]["thumbnails"]["default"]["url"]
                }   
                
            } )
    
        
            index+=1
    
    
if __name__ == "__main__":   
  
    dbname = get_database()
    collection = dbname.YoutubeCollection
    
    

    while True:
        cursor = collection.find()
        for record in cursor:
            # if record["name"] == "code with harry":
            #     continue
            get_responses(record["name"])
        
        time.sleep(120)