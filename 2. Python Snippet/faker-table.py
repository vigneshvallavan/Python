from faker import Faker
import csv
import datetime

fake = Faker()

csvFile = open("faker-data.csv",'w')

headers =  ["ID","Name", "Birth Date", "Phone Number", "Email Id", "Address", "Date", "Time", "Link", "Text"]

writer = csv.DictWriter(csvFile, fieldnames=headers)

writer.writeheader()

userId = 1

for i in range(100):

    writer.writerow({
        "ID" : userId,
        "Name": fake.name(),
        "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
        "Phone Number" : fake.phone_number(),
        "Email Id" : fake.email(),
        "Address" : fake.address(),
        "Date" : fake.date(),
        "Time": fake.time(),
        "Link": fake.url(),
        "Text": fake.word(),
        })
        
    userId+=1

print("CSV generation complete!")

