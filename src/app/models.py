class Place:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Review:
    def __init__(self, user, place, rating, comment):
        self.user = user
        self.place = place
        self.rating = rating
        self.comment = comment
