class Song:
    def __init__(self, title, artist_name, year_purchased, category):
        self.title = title
        self.artist_name = artist_name
        self.year_purchased = year_purchased
        self.category = category

    def __str__(self):
        return "Title: " + self.title + " Artist/Band name: " + self.artist_name +\
               " Year Purchased: " + str(self.year_purchased) + " Category: " + self.category

    def __eq__(self, other):
        if not isinstance(other, Song):
            return NotImplemented
        return self.title == other.title and self.artist_name == other.artist_name and \
            self.year_purchased == other.year_purchased and self.category == other.category

