from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title': '월-E'})
print("target_movie : ", target_movie)
target_star = target_movie['star']
print("target_star : ", target_star)

movies = list(db.movies.find({'star': target_star}))

# for movie in movies
