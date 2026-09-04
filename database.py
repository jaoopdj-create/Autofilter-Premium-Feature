from pymongo import MongoClient, ASCENDING, DESCENDING

class FileDB:
    def __init__(self, uri, database_name):
        self.client = MongoClient(uri, serverSelectionTimeoutMS=10000)
        self.db = self.client[database_name]
        self.files = self.db.files
        self.files.create_index([("name", ASCENDING)])
        self.files.create_index([("created_at", DESCENDING)])

    def add_file(self, data):
        return self.files.update_one(
            {"file_unique_id": data["file_unique_id"]},
            {"$set": data},
            upsert=True
        )

    def search(self, query, limit=20):
        regex = {"$regex": query, "$options": "i"}
        return list(self.files.find({"name": regex}).sort("created_at", -1).limit(limit))

    def count(self):
        return self.files.count_documents({})
