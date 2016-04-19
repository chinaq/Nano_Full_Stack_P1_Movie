import media, fresh_tomatoes

# create movie avatar
avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/" 
                     + "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# create movie game of thrones 
game_of_thrones = media.Movie("Game of Thrones",
                              "https://upload.wikimedia.org/wikipedia/en" 
                              + "/d/d8/Game_of_Thrones_title_card.jpg",
                              "https://www.youtube.com/watch?v=522l0YE9hRQ")

# create movie san andreas
san_andreas = media.Movie("San Andreas",
                          "https://upload.wikimedia.org/wikipedia/en" 
                          + "/3/38/San_Andreas_poster.jpg",
                          "https://www.youtube.com/watch?v=23VflsU3kZE")                          

# creat a movie list
movies = [avatar, game_of_thrones, san_andreas]
# show the movies page
fresh_tomatoes.open_movies_page(movies)
