import azure.functions as func
import pymongo
import os
import ssl

def main(req: func.HttpRequest) -> func.HttpResponse:
    print("entering create advertisement __________--------------================")
    request = req.get_json()

    if request:
        try:
            url = "mongodb://nd-db:dJhfzUf1gYswJG9HYgl8sddJTb0Rc8GaurrWRNOAfMDSAwKr0JjsdM7dUO514KjgfNLRjtZctT8TuhAQqwV9yQ==@nd-db.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@nd-db@"
            client = pymongo.MongoClient(url,  ssl_cert_reqs=ssl.CERT_NONE)
            database = client['nd-db-mongo']
            collection = database['advertisements']
            
            print("request:", request)
            rec_id1 = collection.insert_one(request)
            


            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )