__author__ = 'bhavik'

import webbrowser


class Movie:
    """ This class provides movie title, info and shows trailer """

    def __init__(self, title, info, trailer, thumbnail):
        self.title = title
        self.info = info
        self.trailer_youtube_url = trailer
        self.poster_image_url = thumbnail

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
