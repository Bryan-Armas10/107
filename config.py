import pymongo
import certifi

con_string = "mongodb+srv://bryanarmas:SuperGohan10@cluster0.smufy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("project1")