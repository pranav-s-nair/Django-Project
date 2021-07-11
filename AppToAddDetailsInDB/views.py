import requests
from django.shortcuts import render, redirect
from AppToAddDetailsInDB.models import Students, PopulationCount
from django.http import HttpResponse
import base64
import csv


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "upload.html")
    else:
        file = request.FILES["fileToUpload"].read().decode('UTF-8',errors='replace')
        # file.save()
        # csvFile = csv.DictReader(file)
        # file = bytes(request.FILES["fileToUpload"])
        # decoded = file.decode('UTF-8',errors='replace')
        flag = 0
        lines = file.split("\r\n")
        for line in lines:
            if flag ==0 or len(line)==0:
                flag=1
                continue
            print(line)
            feilds = line.split(',')
            id=feilds[0]
            roll = feilds[1]
            cls = feilds[2]
            fname = feilds[3]
            lname = feilds[4]
            student = Students(id=id,rollnumber=roll, class_field=cls, fname=fname, lname=lname)
            student.save()
        return redirect('/show')


# Create your views here.

def show(request):
    students = Students.objects.all()
    return render(request, "upload.html", {'student': students})

def apiCall(request):
    req = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
    json = req.json()
    print(json)
    # for data in json:
    for data in json['data']:
        year = data["Year"]
        Country = data["Nation"]
        popu= data["Population"]
        val = PopulationCount(year=year,country=Country,population=popu)
        val.save()
    return redirect('/showAPI')

def showAPIVal(request):
    population = PopulationCount.objects.all()
    return render(request, "upload.html", {'population': population})