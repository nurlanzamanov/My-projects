import datetime
import math
import json
import re
import sys


def json_export(records):
    with open ('dataset.json', 'w') as f:
        json.dump(records,f,indent=4)


def counts_in_ranges(records):
    ranges={'low':0,"mid":0,'high':0}
    for record in records:
        if record['score']<=0.3:
            ranges['low']=ranges.get('low')+1
        elif record['score']<=0.6:
            ranges['mid']=ranges.get('mid')+1
        else:
            ranges['high']=ranges.get('high')+1
    print(f'Number of low scores: {ranges["low"]}\nNumber of mid scores: {ranges["mid"]}\nNumber of high scores: {ranges["high"]}')
        


def uni_emails(records):
    emails=[]
    for record in records:
        emails.append(record['email'])
    print(f'The number of unique emails: {len(set(emails))}')
    print(f'The number of unique emails: {len({r['email'] for r in records})}')

def avg(records,key):
    values=[]
    for record in records:
        values.append(record[key])
    mean=sum(values)/len(records)
    print(f'Avg {key}: {mean}')
    print(f'Max {key}: {max(values)}')
    print(f'Min {key}: {min(values)}')
    return mean,values
    

def stats(records):
    print(f'total records:{len(records)}')
    mean,scores=avg(records,key='score')
    sum_dev=0
    for score in scores:
        diff=score-mean
        sum_dev+=diff**(2)
    if len(records)>1:
        sum_dev=sum_dev/(len(records)-1)
        print(f"The standart deviation: {math.sqrt(sum_dev)}")
    avg(records,key='age')
    uni_emails(records)
    counts_in_ranges(records)


def email_validation(email):
    if re.search(r'@',email):
        return email
    else:
        return False

def get_info():

    while True:
        name=input('Enter name:').strip()
        if name:
            break
        else:
            print('The name mustn`t be empty.')

    while True:
        try:
            age=int(input('Enter age:'))
            if 0<=age<=100:
                break
            else:
                print('The age must be between 0 and 100.')
        except ValueError:
            print('The age must be an int.')
    while True:
        email=email_validation(input('Enter email:').strip())
        if email:
            break
        else:
            print('The email must have @.')

    while True:
        try:
            score=float(input('Enter score:'))
            if 0<=score<=1:
                break
            else:
                print('The score must be between 0 and 1.')
        except ValueError:
            print('The score must be a float.')

    record={'name':name, 'age': age, 'email': email, 'score':score}
    return record

def add_record(records,id):
    record=get_info()
    record['id']=id
    record['date']=datetime.datetime.now().isoformat()
    records.append(record)
    id+=1
    return id


    

def main():
    records=[]
    id=1
    while True:
        
        print('AI DATASET TOOL\n1 Add record\n2 Show dataset\n3 Show statistics\n4 Export JSON\n5 Exit')
        choice=input('Enter your choice: ')

        match choice:
            case '1':
                id=add_record(records,id)

            case '2':
                for r in records:
                    print(r)

            case '3':
                stats(records)
                
            case'4':
                json_export(records)
            case '5':
                sys.exit()
            case _:
                print('Wrong choice.')

if __name__=='__main__':
    main()
