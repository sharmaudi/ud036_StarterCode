class Media:
    def __init__(self, title):
        """
        Constructor for the Media class. This method will initialize a new Media object.
        :param title: Media title
        """
        self.title = title


class Movie(Media):
    def __init__(self, title, trailer_youtube_url, poster_url):
        """
        Constuctor for the Movies class. This method will initialize a new Movie object.
        :param title: Movie title.
        :param trailer_youtube_url: Youtube url for the movie trailer
        :param poster_url: Image url for the Movie poster
        """
        super().__init__(title)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_url = poster_url
