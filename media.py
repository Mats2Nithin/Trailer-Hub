# Import statements webbrowser library
import webbrowser


# Definition of movie class
class Movie():
    # Init function(Constructor)
    def __init__(self,movie_title,movie_storyline,
                 poster_image,trailer_youtube):
        # Data members of the class with its initialisation
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    # Member functions
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
