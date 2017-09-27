#Team SuperTele
#Tiffany Moi and Samantha Ngo
#SoftDev1 pd7
#HW05--Jinja Tuning
#2017-09-27

import csv
import sys
import random

from flask import Flask, render_template
app = Flask(__name__)

occupations  = open("occupations.csv", "r")
jobs = csv.reader(occupations)#module parses csv file
dictionary = {"Jobs":[] , "Percent":[]}#master dictionary
job_type = []
percent = []

for row in jobs:
    try:
        #adds job type and percent to lists
        percent.append(float(row[1]))
        job_type.append(row[0])
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

#makes a list of numbers so that you can use a for loop in the template
def getLength():
    l = len(dictionary["Jobs"])
    i = 0
    order = []
    while i < l:
        order.append(i)
        i = i + 1
    return order

@app.route("/")
def home():
    return 'Check out this cool <a href = "/occupations">page</a>'

@app.route("/occupations")
def occupationSetup():
    return render_template('temp.html', dict = dictionary,length = getLength(), job = random_job())

if __name__ == "__main__":
    app.debug = True
    app.run()
