__author__ = 'bhavik'

# import required modules
import media
import fresh_tomatoes


# create new Movie objects by instantiating Movie class in media module
victor_frank = media.Movie("Victor Frankenstein", "Daniel Radcliffe stars in this reimagining of the Frankenstein "
                           "mythos that focuses on Igor, the hunchbacked assistant of the mad scientist responsible "
                           "for patching together a living dead monster.",
                           "https://www.youtube.com/watch?v=UQF2d0gqPDI&index=1&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-",
                           "http://images.fandango.com/r97.6/ImageRenderer/168/250/redesign/static/img/default_poster."
                           "png/183473/images/masterrepository/fandango/183473/victor.jpg")

sinister2 = media.Movie("Sinister 2", "The Citadel director Ciaran Foy takes the helm for this horror sequel penned "
                        "by original Sinister screenwriter C.",
                        "https://www.youtube.com/watch?v=30tgB4J0k5Y&index=2&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-",
                        "http://images.fandango.com/r97.6/ImageRenderer/168/250/redesign/static/img/default_poster.png/"
                        "179599/images/masterrepository/fandango/179599/sinister2poster.jpg")

martian = media.Movie("The Martian", "After an exploratory mission goes awry, lone astronaut Mark Watney (Matt Damon) "
                      "is left for dead on the hostile surface of Mars",
                      "https://www.youtube.com/watch?v=ErkgC-8BfnE&index=3&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-",
                      "http://images.fandango.com/r97.6/ImageRenderer/164/250/redesign/static/img/default_poster.png/0/"
                      "images/masterrepository/fandango/183474/themartian-ps-1.jpg")

hateful_eight = media.Movie("The Hateful Eight", "The Hateful Eight",
                            "https://www.youtube.com/watch?v=nIOmotayDMY&index=4&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7j"
                            "zFy-", "http://images.fandango.com/r97.6/ImageRenderer/168/250/redesign/static/img/default"
                            "_poster.png/185166/images/masterrepository/fandango/185166/thehateful8-teaser-poster.jpg")

hitman = media.Movie("Hitman", "An international assassin known only as Agent 47 (Timothy Olyphant) carries out "
                     "high-profile hits for a mysterious organization",
                     "https://www.youtube.com/watch?v=pjGOr5D_2Tk&index=5&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-",
                     "http://images.fandango.com/r97.6/ImageRenderer/164/250/redesign/static/img/default_poster.png/0/"
                     "images/masterrepository/fandango/106492/hitmanposter1.jpg")

ride_along2 = media.Movie("Ride Along 2", "The action moves to Miami in this sequel to the 2014 comedy hit.",
                          "https://www.youtube.com/watch?v=2t5Q2SpaiNo&index=6&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-",
                          "http://images.fandango.com/r97.6/ImageRenderer/164/250/redesign/static/img/default_poster."
                          "png/0/images/masterrepository/fandango/185715/ridealong2.jpg")


# create new movie list to be added to final web page
movie_list = [victor_frank, sinister2, martian, hateful_eight, hitman, ride_along2]
# generate new movie page by calling function open_movies_page inside fresh_tomatoes module
fresh_tomatoes.open_movies_page(movie_list)
