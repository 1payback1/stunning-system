# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def fun1(list_of_dics = movies):
    print('Enter name of the movie:')
    name = str(input())
    flag = 0
    for x in movies:
        if name in x.values():
            flag = 1
    
    if flag == 1:
        for x in movies:
            if name == x['name']:
                if x['imdb'] > 5.5:
                    return True
                else:
                    return False
    else:
        print('There is no movie with that name')
        return False
        
#2
def sublist(list_of_dics = movies):
    sublist = []
    for x in list_of_dics:
        if x['imdb'] > 5.5:
            sublist.append(x['name'])
    return sublist

#3
def category(list_of_dics = movies):
    my_list = []
    print('Enter category:')
    my_category = str(input())
    for x in list_of_dics:
        if my_category in x.values():
            my_list.append(x['name'])
    return my_list

#4
def average_imdb_by_names(list_of_dics = movies):
    print('Enter comma-separated names of movies:')
    string_of_movies = str(input())
    list_of_movies = string_of_movies.split(', ')
    number_of_movies = len(list_of_movies)
    total_imdb = 0
    for x in list_of_movies:
        for y in list_of_dics:
            if x in y.values():
                total_imdb += y['imdb']
                break
    return float(total_imdb / number_of_movies)

#5
def average_imdb_by_category(list_of_dics = movies):
    print('Enter category:')
    category = str(input())
    total_imdb = 0
    counter = 0
    for x in list_of_dics:
        if category in x.values():
            counter += 1
            total_imdb += x['imdb']
    return float(total_imdb / counter)