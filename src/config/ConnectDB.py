from pymongo import MongoClient
from GetEnv import GetEnv

class ConnectDB(GetEnv):
    def __init__(self) -> None:
        try:
            self.client = MongoClient(self.get_mongo_url)[self.get_dataname]
            if self.client.list_collection_names() in self.get_collection_name():
                print("collection is exists!")

        except Exception as e:
            exit(f"An error occurred: {e}")

    def get_client(self) -> MongoClient:
        return self.client
