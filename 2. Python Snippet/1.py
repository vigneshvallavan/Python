from faker import Faker
import csv
import datetime
import random

fake = Faker()

csvFile = open("TestData_Initial_Medium.csv",'w')

headers =  ["Policy_number","First_name", "Last_name", "Age", "Gender", "dob", "last_login", "Transaction_id", "Transaction_amt", "Start_ts",
"End_ts","Status_in","Part_num","Create_Batch_key","Update_Batch_key","Email","Phone_Number","IP_Address","Zip_code","Device"]

writer = csv.DictWriter(csvFile, fieldnames=headers)

writer.writeheader()

e = datetime.datetime.now() 

id = 9876543210
id2 = 12345.12

for i in range(1000000):

    gender = random.choice( ["M","F"] )
    age = random.choice([23,24,25,26,27,28,29,30])
    device = random.choice(["Tab","Mobile","Lap","Desktop"])

    writer.writerow({
        "Policy_number" : "A1235069",
        "First_name": "Fname50161",
        "Last_name" : "Fname50160",
        "Age" :age,
        "Gender":gender,
        "dob" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(1971, 1,1)),
        "last_login" : fake.date(),
        "Transaction_id": id,
        "Transaction_amt": id2,
        "Start_ts": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2021, 1,1)),
        "End_ts" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(9999, 1,1)),
        "Status_in": "A",
        "Part_num": 1,
        "Create_Batch_key": str(e.strftime("%Y%m%d%H%M%S")),
        "Update_Batch_key": str(e.strftime("%Y%m%d%H%M%S")),
        "Email" : fake.email(),
        "Phone_Number" : fake.phone_number(),
        "IP_Address" : fake.ipv4(),
        "Zip_code": fake.zipcode(),
        "Device" : device,
        })
        
    id+=1
    id2+=0.01

print("CSV generation complete!")

