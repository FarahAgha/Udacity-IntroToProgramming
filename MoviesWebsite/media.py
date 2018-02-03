import webbrowser
class Movie():
    def __init__(self, title, art_imagery,  trailer,story_line, screenwriter, director, launch_date, duration, genres):
        self.title = title
        self.art_imagery = art_imagery
        self.trailer = trailer
        self.story_line =story_line
        self.director = director
        self.screenwriter = screenwriter
        self.launch_date = launch_date
        self.duration = duration
        self.genres = genres

    def print_movie_info(self):
        print self.title
        print self.story_line
        print self.screenwriter
        print self.director
        print self.launch_date
        print self.duration
        print self.genres

    def show_trailer(self):
        webbrowser.open(self.trailer)

    def show_art_imagery(self):
        webbrowser.open(self.art_imagery)
