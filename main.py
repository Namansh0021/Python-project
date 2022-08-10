import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017")
database= connection["project"]
collection = database["project"]

query={
   "hi":"Hello, How are you?",
   "good": "Well, that's great \n What is your name?",
   "bad": "Well, that's not okay \n What is your name?",
   "naman":"How may I help you? \n"
           "Choose your option \n"
           "a) Link for Google \n"
           "b) Link for youtube \n"
           "c) Link for facebook",
   "a": "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjC_urg-Lb5AhWvjIkEHZiGB8AQPAgI",
    "b":"https://www.youtube.com/",
   "c":"https://www.facebook.com/",
   "services": "We provide muntiple services for managing social account at a single place",
}

print("Type your msg to start ! or press quit to end")

count= 0
while True:
   count += 1
   q1=input()

   if(q1=="quit"):
       print("Chat Closed")
       print("----------------------------------->")
       break
   else:
       document = collection.insert_one({q1: count})
       print(query[q1])