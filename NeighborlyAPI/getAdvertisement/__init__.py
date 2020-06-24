import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5ec34b22b5f7f6eac5f2ec3e

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            url = "mongodb://nd-db:dJhfzUf1gYswJG9HYgl8sddJTb0Rc8GaurrWRNOAfMDSAwKr0JjsdM7dUO514KjgfNLRjtZctT8TuhAQqwV9yQ==@nd-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@nd-db@" # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['nd-db-mongo']
            collection = database['advertisements']
           
            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            print("----------result--------")

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)