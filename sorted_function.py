class Movies:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    def __str__(self):
        return f'{self.name} has a rating of {self.rating}'
    def get_rating(self):
        return self.rating
m1 = Movies("Inception", 8.8)
m2 = Movies ("The Dark Knight", 9.0)
m3 = Movies ("Interstellar", 8.6)
movies_list = [m1, m2, m3]
sorted_movies = sorted(movies_list, key = Movies.get_rating, reverse = True)
for x in sorted_movies:
    print (x)
