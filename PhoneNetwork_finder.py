#!/usr/bin/env python
# coding: utf-8
#Give the directory at the place of Directory_path which has your file
# In[2]:


import phonenumbers,csv
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

def phonenumber_scanner(phone_numbers):
    info = [["Number","Country","Network"]]
    for phonnumber in range(0,len(phone_numbers)):
        number = phonenumbers.parse(phone_numbers[phonnumber])
        description = geocoder.description_for_number(number,"en")
        supplier = carrier.name_for_number(number,"en")
        info.append([phone_numbers[phonnumber],description,supplier])
    data = str(tabulate(info,headers = "firstrow",tablefmt = "fancy_grid"))
    print(data)
    with open('Directory_path(target)','a+') as results:
        writer = csv.writer(results)
        with open('Directory_path(source)','r') as csvfile:
            reader = csv.reader(csvfile)
            record = list(reader)
            if len(record) == 0:
                writer.writerow(info[0])
                for records in range(1,len(info)):
                    writer.writerow(info[records])
            else:
                for records in range(1,len(info)):
                    writer.writerow(info[records])


phone_numbers = []
#If the input is from any csv files
with open('Directory_path(source)','r') as csvfile: 
    reader = csv.DictReader(csvfile)
    for record in reader:
        phone_numbers.append(record['Phone'])

#If the input needs to be given manually
#Enter the input as 1 to stop giving inputs
while(1):
    phone_number = input("Enter Phone Number(s) :")
    if(phone_number == str(1)):
        break
    else:
        phone_numbers.append(phone_number)
phonenumber_scanner(phone_numbers)


# In[ ]:




