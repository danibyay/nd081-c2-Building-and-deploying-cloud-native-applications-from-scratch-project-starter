import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = "mongodb://nd-db:dJhfzUf1gYswJG9HYgl8sddJTb0Rc8GaurrWRNOAfMDSAwKr0JjsdM7dUO514KjgfNLRjtZctT8TuhAQqwV9yQ==@nd-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@nd-db@"
            client = pymongo.MongoClient(url)
            database = client['nd-db-mongo']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

