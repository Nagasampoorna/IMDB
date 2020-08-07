from django.shortcuts import render
from IMDB.settings import IMDB_FILE
from app1.middleware import fetchdata
import json

def showindex(request):
    dict= json.loads(open(IMDB_FILE).read())
    print(dict)
    return render(request,'index.html',{'data':dict})

# Create your views here.
