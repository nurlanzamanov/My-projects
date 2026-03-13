import math
import statistics as st
import datetime as dt
import json
import re   
import random
import sys
from faker import Faker
fake=Faker()

def country_distribution(dataset):
    country_dict={}
    countries=[record['country'] for record in dataset]
    for country in countries:
        country_dict[country]=country_dict.get(country,0)+1
    
    print('The country distribution:')
    for line in country_dict:
        print(line)

def score_distribution(dataset):
    score_dict={}
    scores=[record['score'] for record in dataset]
    for score in scores:
        if 0<=score<=0.2:
            score_dict['0-0.2']=score_dict.get('0-0.2',0)+1
        elif 0.2<=score<=0.4:
            score_dict['0.2-0.4']=score_dict.get('0.2-0.4',0)+1
        elif 0<=score<=0.2:
            score_dict['0.4-0.6']=score_dict.get('0.4-0.6',0)+1
        elif 0<=score<=0.2:
            score_dict['0.6-0.8']=score_dict.get('0.6-0.8',0)+1
        elif 0<=score<=0.2:
            score_dict['0.8-1']=score_dict.get('0.8-1',0)+1
    print('The score distribution:')
    for line in score_dict:
        print(line)
        

def min_max(dataset,key):
    values=[record[key] for record in dataset]
    print(f'Mean {key} is {st.mean(values)}')
    print(f'Min {key} is {min(values)}')
    print(f'Max {key} is {max(values)}')


def stats(dataset,avg_score,std):
    min_max(dataset,'score')
    print(f'The standart deviation of scores is {std}')

    min_max(dataset,'age')
    score_distribution(dataset)
    country_distribution(dataset)


def anomaly_detection(dataset,avg_score):
    sum=0
    scores=[record['score' for record in dataset]]
    for score in scores:
        sum+=(score-avg_score)**2

    std=(sum/len(scores))**(1/2)
    low=avg_score-2*std
    high=avg_score+2*std

    for record in dataset:
        if low<=record['score']<=high:
            record['anomaly']=False
        else:
            record['anomaly']=True
    return std
    


def cleaning(dataset,avg_score):
    for record in dataset:
        if record['score']>1:
            record['score']=1
        elif record['score']<0:
            record['score']=0
        elif record['age']=='invalid':
            record['age']=None
        elif record['email']=='invalid':
            dataset.remove(record)
        elif not record['score']:
            record['score']=avg_score

    

def validation(dataset):
    for num in range(len(dataset)):
        if (
            not dataset[num]['name'] 
            or not isinstance(id,int) 
            or not 0<=dataset[num]['age']<=100 
            or not re.fullmatch(
                r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", 
                dataset[num]['email'])
        ):
            dataset[num]['valid']=False
        else:
            dataset[num]['valid']=True

            
            
def time_comparison(dataset):
    timestamps=[line['time'] for line in dataset]
    print(f'The earliest timestamp is {min(timestamps)}')
    print(f'The lates timestamp is {max(timestamps)}')

    

def avg_score(dataset):
    sum=0
    count=len(dataset)
    for num in len(range(dataset)):
        try:
           sum+=dataset[num]['score']
        except ValueError:
            count-=1
    print(f'The avg score is {sum/count}')
        
    

def duplicate_emails(dataset):
    duplicate={}
    for num in range(len(dataset)):
        if dataset[num]['email'] in duplicate:
            duplicate[dataset[num]['email']]=duplicate.get(dataset[num]['email'])+1
        else:
            duplicate[dataset[num]['email']]=0
    
    for key in duplicate.keys():
        if duplicate[key]>=1:
            print(f'The email {key} has been used {duplicate[key]-1} time extra.')


def missing_values(dataset):
    for num in range(1,len(dataset)+1):
        for key in dataset[num].keys():
            if dataset[num][key]=='invalid' or not 0<=dataset[num][key]<=1:
                print(f'The {num}th line of dataset is missing {key}')

def show_summary(dataset):
    print(f'The number of records: {len(dataset)}')
    missing_values(dataset)
    duplicate_emails(dataset)
    avg_score(dataset)
    time_comparison(dataset)

    return avg_score
    


def load_json():
    dataset_file=input()
    with open(dataset_file) as file:
        dataset=json.load(file)
    return dataset


def generate_syn_dataset(dataset,id):
    id=1
    for _ in range(100):
        if random.random()<0.06:
            id='invalid'
        if random.random()<0.03:
            name='invalid'
        else:
            name=fake.name()    
        if random.ranmdon()<0.05:
            age='invalid'
        else:
            age=random.randint(1,100):
        if random.random()<0.1:
            email='invalid'
        else:
            email=fake.email()
        if random.random()<0.08:
             score=round(random.random(-0.5,1.5))
        else:
            score=round(random.random())
        if random.random<0.05:
            country='invalid'
        else:
            country=fake.country()
        if random.random()<0.05:
            time='invalid'
        else:
            time=dt.datetime.now().date()
        record={
            'id':id,
            'name':name,
            'age':age,
            'email':email,
            'score':score,
            'country':country,
            'time':time,
        }
        dataset.append(record)
        id+=1
    return dataset


def main():
    dataset=[]
    while True:
        choice=int(input('AI DATA PIPELINE TOOL\n1 Generate synthetic dataset\n2 Load dataset from JSON\n3 Show dataset summary\n4 Validate dataset\n5 Clean dataset\n6 Detect anomalies\n7 Generate statistics\n8 Train/Test split\n9 Export cleaned dataset\n10 Exit\n\n Enter your choice: '))
        
        match choice:
            
            case 1:
                dataset=generate_syn_dataset()

            case 2:
                dataset=load_json()

            case 3:
                avg_score=show_summary(dataset)

            case 4:
                validation(dataset)

            case 5:
                cleaning(dataset,avg_score
                         )
            case 6:
                std=anomaly_detection(dataset)

            case 7:
                stats(dataset,avg_score,std)

            case 8:

            case 9:

            case 10:

            case _:
                print('There is no such choice.')
