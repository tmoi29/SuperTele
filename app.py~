import csv
import sys
import random

occupations  = open("occupations.csv", "r")
jobs = csv.reader(occupations)#module parses csv file
dictionary = {"Jobs":[] , "Percent":[]}#master dictionary
job_type = []
percent = []

for row in jobs:
    try:
        #adds job type and percent to lists
        job_type.append(row[0])
        percent.append(float(row[1]))
    except:
        pass

#inputs lists of job type and percent into dictionary
dictionary["Jobs"] = job_type
dictionary["Percent"] = percent

def random_job():
    """generate a random number, subtract the percents, last one
     to go over is the desired job"""
    num = random.random()*100
    i=-1
    while num>0:
        i+=1
        num-=dictionary["Percent"][i]
    return dictionary["Jobs"][i]
        
print(random_job())
