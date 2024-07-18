import os

class GetEnv:

    @staticmethod
    def get_mongo_url() -> str:
        return os.getenv("MONGO_URL", "mongodb://localhost:27017")
    
    @staticmethod
    def get_dataname() -> str:
        return os.getenv("MONGO_DATANAME", "symbols_predict")
    
    @staticmethod
    def get_collection_name() -> str:
        return os.getenv("MONGO_COLLECTION_NAME", "")

    @staticmethod
    def get_port() -> int:
        return os.getenv(int("PORT"), 50051)
    
    @staticmethod
    def get_api_secret() -> str:
        return os.getenv("API_SECRET", "nquFquj6eKLmvgWJ4Er6SlFYFte8b0auIKfFmKUH0A7Fh6Mg7FGKb97PPgZggXnO")

    @staticmethod
    def get_api_key() -> str:
        return os.getenv("API_KEY", "dhxyexgq56p8qfXIXdkL40DOTfpopgBysz8IEbvxJfuqksbDphNubGS8ydMFJTA")
