import subprocess
from pymongo import MongoClient

# Try connecting to Database
connection = None
i = 0
while i < 10:
	try:
			connection = MongoClient('mongodbsc', 27017)
			print("Successfully connected to mongodb")
			break
	except:
			print("Will retry connecting to mongodb")
	i = i +1

# Check whether collection accounts exists in schulcloud db
db = connection['schulcloud']
exists = "accounts" in db.collection_names()
print("Accounts in schulcloud exists: " + str(exists))
# depending on existence start seeding db or start server
if exists:
	print("Starting the server now")
	subprocess.call("./start.sh")
else:
	print("Seeding the Database now")
	subprocess.call("./seed.sh")
	subprocess.call("./start.sh")
