Instructions = '''

Generating Random IDs
Add Command: py -3.6 generateDeviceID.py -c add -n <number of accounts to add>
Delete Command:  py -3.6 generateDeviceID.py -c del --id <ID>
View Command: py -3.6 generateDeviceID.py -c view
Delete All [This will kill your database, use wisely]: py -3.6 generateDeviceID.py -c del-all
Search by ID: py -3.6 generateDeviceID.py -c view -id <ID>

'''

import argparse
from random import randint as ri
import pymongo
import datetime
parser = argparse.ArgumentParser(description='Generate New Device-ID')
parser.add_argument('-n', '--devices',help="Enter the number of device IDs to be generated.",type=int)
parser.add_argument('-c', '--choice',help="Enter the choice.",type=str,required=True)
parser.add_argument('-i', '--id',help="Enter the id",type=str)
from bson.objectid import ObjectId
idSize = 12
client = pymongo.MongoClient("mongodb+srv://admin-user:ogimljVnqPClQI5i@cluster0-8qxz0.mongodb.net/mywatertech?retryWrites=true&w=majority")
db = client["mywatertech"]
collection = db["rdevices"]


def GetTimeStamp():
    timestamp = str(datetime.datetime.now()).split(":")
    try:return(timestamp[0]+":"+timestamp[1]+ " hrs")
    except: return(str(datetime.datetime.now()))

def AddId(idnumber):
    for i in range(args.devices):
        generated=""
        for j in range(idSize):
            generated+=character[ri(0,len(character)-1)]
        array.append(generated)
    print("Following IDs are to be added:")
    for i in array:
        _id = collection.insert({"timestamp":GetTimeStamp(),"status":"Inactive"})    
        print(_id)
    print("Add Success!")

def DeleteID(ids):
    deleteresult = collection.find_one({"Device-ID": ids})
    if deleteresult is None:
        print("ID entered is non-existent in current database. Exiting...")
    else:
        collection.delete_one({"Device-ID": ids})
        print(f"Delete succeeded for id = {ids}")
def DeleteAll():
    result = collection.find({})
    with open("backup.txt","w+") as f:
        for res in result:f.write(str(res)+"\n")
    deleted = collection.delete_many({})
    print("Deleted All IDs. A Backup of all the IDs can still be seen in backup.txt. But they can't be associated to new account.")

def ViewID(idx):
    if not(idx):
        result = collection.find({})
        print("Fetched results: ")
        for i in result:
            print(i)
    else:
        res = collection.find_one({"_id": ObjectId(idx)})
        print(f"Found result:-\n {res}")

args = parser.parse_args()
array=[]
generated=""
if args.choice == "del":
    if not(args.id):
        print("Invalid delete operation: Id is must. try: 'python generateDeviceID.py -choice del -id <ID TO DELETE>'")
    else:
        decision=input(f"Are you sure you want to delete the device entry with ID:{args.id}? (Y/N).")
        if decision =="Y" or decision == "y":
            DeleteID(args.id)
        else:
            print("Delete Operation Aborted, Exiting")
        
elif args.choice=="add":
    if args.devices and args.choice == 'add':
        AddId(args.devices)
    else:
        AddId(1)
elif args.choice == "view":
    if not(args.id):ViewID(0)
    else:ViewID(args.id)
elif args.choice == "del-all":
    choice = input("Are you 100% sure you want to clear off all the devices? (Y/N)")
    if choice.lower() == "y":DeleteAll()
    else:print("Delete all operation aborted! Quitting")
else:
    print(f"\n\nInvalid query, Please use any of the following queries to execute: {Instructions}")




