from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.messages import error
from IMDB.settings import IMDB_FILE
from app1.middleware import fetchdata
import json
def dict_data():
    dict_data = json.loads(open(IMDB_FILE).read())
    id =  [x['id'] for x in dict_data if
             x['id']!= ''and  x['title'] != '' and x['year'] != '' and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != ''and x['rating_votes'] != ''and x[
                  'plot'] != '']
    titles = [x['title'][0:len(x['title']) - 1] for x in dict_data if
              x['id'] != '' and x['title'] != '' and x['year'] != '' and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != ''and x['rating_votes'] != ''and x[
                  'plot'] != '']
    year = [x['year'] for x in dict_data if
            x['id'] != '' and x['title'] != ''and x['year'] != ''and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x['rating_votes'] != ''and x[
                   'plot'] != '']
    length = [x['length'] for x in dict_data if
              x['id'] != '' and x['title'] != '' and x['year'] != ''and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x[      'rating'] != '' and x['rating_votes'] != '' and x[
                  'plot'] != '']
    posters = [x['poster'] for x in dict_data if
               x['id'] != '' and x['title'] != ''and x['year'] != ''and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x['rating_votes'] != '' and x[
                   'plot'] != '']
    trailer_links = [x['trailer']['link'] for x in dict_data if
                     x['id'] !='' and x['title'] != ''and x['year'] != ''and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x['rating_votes'] != '' and x[
                         'plot'] != '']
    ratings = [x['rating'] for x in dict_data if
               x['id'] != '' and x['title'] != '' and x['year'] != ''and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x['rating_votes'] != '' and x[
                   'plot'] != '']
    rating_votes = [x['rating_votes'] for x in dict_data if
               x['id'] != '' and x['title'] != '' and x['year'] != ''and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x['rating_votes'] != '' and x[
                   'plot'] != '']

    plots = [x['plot'] for x in dict_data if
             x['id'] != '' and x['title'] != ''and x['year'] != ''and x['length'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x['rating_votes'] != '' and x[
                 'plot'] != '']

    index = [{'id':id,'title': title,'year':year,'length':length, 'poster': poster, 'rating': rating,'rating_votes':rating_votes, 'plot': plot, 'trailer': trailer} for
               id,title,year,length, poster, rating,rating_votes, plot, trailer in zip(id,titles,year,length, posters, ratings,rating_votes, plots, trailer_links)]
    return index
def showindex(request):
    index = dict_data()
    return render(request, 'index.html', {'data': index})
def searchMovie(request):
    name = request.GET.get('movieName')
    print(name)
    index = dict_data()
    for x in index:
        if x['title'] == name:
            print(x)
            return render(request, 'search_movie.html', {'search_movie':x})
    else:
        error(request, 'enter another movie name')
        return HttpResponse('Please Enter Correct Movie Name')

# def showindex(request):
#     dict_data = json.loads(open(IMDB_FILE).read())
#     print(dict_data)
#     return render(request,'index.html',{'data':dict_data})

# Create your views here.
# def searchMovie(request):
#     name = request.GET.get('movieName')
#     dict_data = showindex(request)
#     print(name)
#     # print(dict_data)
#
#     for x in dict_data:
#         if x.title == name:
#             print(x)
#             return render(request,'search_movie.html',{'search_movie': x})
#     else:
#         error(request,'enter another movie name')
#         return HttpResponse('Please Enter Correct Movie Name')
