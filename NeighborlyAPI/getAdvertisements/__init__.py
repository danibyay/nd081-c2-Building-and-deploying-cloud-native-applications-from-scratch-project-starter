import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os
import ssl

def main(req: func.HttpRequest) -> func.HttpResponse:
    print("hola dani")
    try:
        url = "mongodb://nd-db:dJhfzUf1gYswJG9HYgl8sddJTb0Rc8GaurrWRNOAfMDSAwKr0JjsdM7dUO514KjgfNLRjtZctT8TuhAQqwV9yQ==@nd-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@nd-db@"
        client = pymongo.MongoClient(url,  ssl_cert_reqs=ssl.CERT_NONE)
        print("mongoclient is {}".format(client))
        database = client['nd-db-mongo']
        collection = database['advertisements']

        
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

