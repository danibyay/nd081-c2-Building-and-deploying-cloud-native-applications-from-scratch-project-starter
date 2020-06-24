import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os
import ssl

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://nd-db:dJhfzUf1gYswJG9HYgl8sddJTb0Rc8GaurrWRNOAfMDSAwKr0JjsdM7dUO514KjgfNLRjtZctT8TuhAQqwV9yQ==@nd-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@nd-db@"
            client = pymongo.MongoClient(url, ssl_cert_reqs=ssl.CERT_NONE)
            database = client['nd-db-mongo']
            collection = database['posts']

            query = {'_id': id}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)