from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    records = {}
    url = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    inshorts_data = url.json()
    records['alldata'] = inshorts_data
    return render(request, 'index.html', records)

def spnews(request):
    records = {}
    url = requests.get("https://inshorts.me/news/topics/sports")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request,'spnews.html',records)

def topnews(request):
     records = {}
     url = requests.get("https://inshorts.me/news/top?offset=0&limit=21")
     inshorts_data = url.json()
     records['topdata'] = inshorts_data
     return render(request,'topnews.html',records)

def scinews(request):
    records = {}
    url = requests.get("https://inshorts.me/news/topics/science")
    inshorts_data = url.json()
    records['sciencedata'] = inshorts_data
    return render(request,'scinews.html',records)

def trendnews(request):
     records = {}
     url = requests.get("https://inshorts.me/news/trending?offset=0&limit=21")
     inshorts_data = url.json()
     records['trendingdata'] = inshorts_data
     return render(request,'trendnews.html',records)

def entnews(request):
     records = {}
     url = requests.get("https://inshorts.me/news/topics/entertainment")
     inshorts_data = url.json()
     records['entertainmentdata'] = inshorts_data
     return render(request,'entnews.html',records)



