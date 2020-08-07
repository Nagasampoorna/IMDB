import json
class IMDB_MOVIE:

    def __init__(self,get_response):
         self.get_response = get_response
         print('i am call')
         fetchdata()
    def __call__(self, request,*args, **kwargs):
        response = self.get_response(request)
        return response
def fetchdata():
    import requests
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

    querystring = {"purchaseCountry": "India", "homeCountry": "India", "currentCountry": "India"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "0d01940e33mshac5e0d979435657p178021jsnffd5a118208f"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    list_data = []
    count = 0
    for x in data:
        movie_id = x.split('/')[2]
        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+movie_id
        headers = {
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
            'x-rapidapi-key': "0d01940e33mshac5e0d979435657p178021jsnffd5a118208f"
        }
        response = requests.request("GET", url, headers=headers)
        dict_data = json.loads(response.text)
        if dict_data['title'] and dict_data['poster']:
            list_data.append(dict_data)
            count += 1
            if count == 10:
                break
    json.dump(list_data,open('app1/raw/imdb.json','w'))
    print("Data Written To File")