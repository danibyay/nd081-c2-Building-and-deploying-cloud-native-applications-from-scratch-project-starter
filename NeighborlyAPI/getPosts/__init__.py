import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://nd-db:dJhfzUf1gYswJG9HYgl8sddJTb0Rc8GaurrWRNOAfMDSAwKr0JjsdM7dUO514KjgfNLRjtZctT8TuhAQqwV9yQ==@nd-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@nd-db@"
        client = pymongo.MongoClient(url)
        database = client['nd-db-mongo']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)