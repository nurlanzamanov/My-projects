import datetime
import math
import json
import re
import array
import random
import sys

def email_validation(email):
    if re.search(r'@',email):
        return email
    else:
        return False

def get_info():
    name=int(input('Enter name:')).strip()
    while True:
        try:
            age=int(input('Enter age:'))
            break
        except ValueError:
            print('The age must be an int.')
    while True:
        try:
            email=email_validation(input('Enter email:').strip())
            break
        except False:
            print('It is not an email.')

    while True:
        try:
            score=float(input('Enter score:'))
            break
        except ValueError:
            print('The score must be a float.')

    record={'name':name, 'age': age, 'email': email, 'score':score}
    return record

def add_record(records,id):
    record=get_info()
    records.append({id:record})
    id+=1
    return id


    

def main():
    records=[]
    id=0
    while True:
        
        print('AI DATASET TOOL\n1 Add record\n2 Show dataset\n3 Show statistics\n4 Export JSON\n5 Exit')
        choice=input('Enter your choice: ')

        if choice=='1':
            add_record()

        elif choice=='2':
            print(records)

        elif choice=='3':
            
        elif choice=='4':
            print(json_file=json.dump(records))
        elif choice=='5':
            sys.exit()
        else:
            print('Wrong choice.')